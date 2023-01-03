#include <AP_Sync.h>  //library for Arduino control from Processing

AP_Sync streamer(Serial);  //allows AP_Sync to use Serial communication


int SpinPins[6] = { 4, 5, 6, 7, 8, 12 };           //the pins used for spinning motor
int SpinPinsLen = sizeof(SpinPins) / sizeof(int);  //length of the array holding the pins
int LEDpins[3] = { 9, 10, 11 };                    //pins used for LED control (RGB) - MUST BE PWM PINS
int LEDpinsLen = sizeof(LEDpins) / sizeof(int);
int DoorPins[2] = { 2, 3 };  //pins used for door sensors - MUST BE INTERRUPT PINS
int DoorPinsLen = sizeof(DoorPins) / sizeof(int);

//init values for LED colour
int redVal = 0;
int greenVal = 0;
int blueVal = 0;

//init spin speed
int spinSpeed = 0;

bool doorOpen = true;  //boolean to hold if door open or closed
bool emrgStop = false;  //true if emergenct stop pressed
int emergencyStop = 0;  //holds value from serial

const byte availableBytes = 12;
char incomingSerial[availableBytes];  //holds the incoming serial data
bool serialData = false;              //will change when data is sent

void setup() {
  Serial.begin(9600);

  //decide if the doors are open or closed at start
  if ((digitalRead(DoorPins[0]) == LOW) && (digitalRead(DoorPins[1]) == LOW)) {
    doorOpen = false;
    Serial.println("DOOR CLOSE @ START");
  } else {
    doorOpen = true;
    Serial.println("DOOR OPEN @ START");
  }

  //declare pinMode for spin motor controller pins
  for (int i = 0; i < SpinPinsLen; i++) {
    pinMode(SpinPins[i], INPUT);
    Serial.println(SpinPins[i]);  //DEBUG prints to serial once been initialised
  }
  //declare pinMode for LED pins
  for (int i = 0; i < LEDpinsLen; i++) {
    pinMode(LEDpins[i], OUTPUT);
    Serial.println(LEDpins[i]);  //DEBUG prints to serial once been initialised
  }
  //declare pinMode for door sensor pins
  for (int i = 0; i < DoorPinsLen; i++) {
    pinMode(DoorPins[i], INPUT_PULLUP);
    Serial.println(DoorPins[i]);  //DEBUG prints to serial once been initialised
    attachInterrupt(digitalPinToInterrupt(DoorPins[i]), doorOPENED, FALLING);
  }

  setLEDColour(255, 0, 40);  //sets lights pink to start
}

void doorOPENED() {  //what to do if door is open
  doorOpen = true;
  setLEDColour(255, 0, 0);  //set lights red
  //keep running this loop if ANY doors are open
  while (doorOpen == true) {
    //will break the while loop if the door is shut
    if ((digitalRead(DoorPins[0]) == LOW) && digitalRead(DoorPins[1]) == LOW) {
      doorOpen = false;
      processDoorState(2, 0, 255, 0);
    } else {
      processDoorState(1, 255, 0, 0);
    }
    //delay to prevent saturating the serial line
    delay(100);
  }
  setLEDColour(redVal, greenVal, blueVal);
}

void processDoorState(int state, int red, int green, int blue) {
  if (state == 1)
    streamer.sync("doorState", "OPEN");
  else if (state = 2) {
    streamer.sync("doorState", "CLOSED");
  }
}

void setLEDColour(int redLED, int greenLED, int blueLED) {
  //ensure the value between 0&255 and inverts as common annode
  redLED = 255 - constrain(redLED, 0, 255);
  greenLED = 255 - constrain(greenLED, 0, 255);
  blueLED = 255 - constrain(blueLED, 0, 255);

  //writes the values to the led
  analogWrite(LEDpins[0], redLED);
  analogWrite(LEDpins[1], greenLED);
  analogWrite(LEDpins[2], blueLED);

  //Serial.println("LED COLOUR SET");
}

void recvSerial() {
  static byte count = 0; //counter - use of static byte to retain value

  while (Serial.available() > 0 && serialData == false) { //loops if no data is received
    char readChar = Serial.read();  //reads each character from the serial line
    char endMarker = '\n';  //must store the 'enter' key as a character to compare

    if (readChar != endMarker) {
      incomingSerial[count] = readChar; //appends the new character to the array holding all received data
      count++;

      if (count >= availableBytes) {  //will overwrite data if exceeded
        count = availableBytes - 1;
      }
    } else {
      incomingSerial[count] = '\0'; //used to terminate the string
      count = 0;  //reset the count
      serialData = true;  //allows others to realise data has been received
    }
  }
  if (serialData == true) {
    splitSerial();
  }
}

void splitSerial() {
  //incoming data defined by the following order:
  //1st char emergency stop
  //2,3,4 red LED value
  //5,6,7 green LED value
  //8,9,10 blue LED value
  //11 spin speed setting 

  emergencyStop = incomingSerial[0] - '0';  //subtract '0' to convert ASCII to int
  if(emergencyStop == 1){
    setLEDColour(255,0,0);
  }

  //convert the LED array values into one int per colour
  redVal = calcActualValue(incomingSerial[1], incomingSerial[2], incomingSerial[3]);
  greenVal = calcActualValue(incomingSerial[4], incomingSerial[5], incomingSerial[6]);
  blueVal = calcActualValue(incomingSerial[7], incomingSerial[8], incomingSerial[9]);

  spinSpeed = incomingSerial[10]; //set spin speed
}


//combines array values into one int for LED values
int calcActualValue(int hundred, int ten, int one) {
  int Val100 = hundred - '0'; //determines the hundreds, tens and units
  int Val10 = ten - '0';
  int Val1 = one - '0';
  int ValCalc = (Val100 * 100) + (Val10 * 10) + Val1; //adds the values to give the original int
  //validates the value is acceptable for LED value
  if (ValCalc >= 0 && ValCalc <= 255) {
    return ValCalc;
  }
  else{
    return 0;
  }
}

//used to print the data received on the serial line stored in 'incomingSerial[]'
void printSerial() {
  if (serialData == true) { //checks data is actually waiting
    Serial.print("RECEIVED:..."); 
    Serial.println(incomingSerial);
    serialData = false; //declares the data as dealt with
  }
}

void loop() {
  //check initial state of doors before allowing remaining code to run
  if (doorOpen == true) {
    doorOPENED();
  }
  recvSerial();
  printSerial();
}
