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

bool doorOpen = true;  //boolean to hold if door open or closed

char incomingSerial[64];
int availableBytes = 0;



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

  setLEDColour(255, 0, 40); //sets lights pink to start

}

void doorOPENED() {  //what to do if door is open
  doorOpen = true;
  setLEDColour(255, 0, 0); //set lights red
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
  streamer.sync("Red", red);
  streamer.sync("Green", green);
  streamer.sync("Blue", blue);
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

  Serial.println("LED COLOUR SET");
}



void loop() {
  //check initial state of doors before allowing remaining code to run
  if (doorOpen == true) {
    doorOPENED();
  }

  while (Serial.available() > 0) {
    //finds integers in order and puts into variables
    int emergStop = Serial.parseInt();  //defines if emergency stop triggered (0/1)
    if (emergStop == 1) {
      Serial.println("EMERGENCY STOP"); //prints to the serial line
      setLEDColour(255,0,0); //sets the lights to red
      Serial.end(); //stops all serial to clear it
      Serial.begin(9600); //restarts the serial fresh
    }
    redVal = Serial.parseInt();     //int for red value (0-255)
    greenVal = Serial.parseInt();   //int for green value (0-255)
    blueVal = Serial.parseInt();    //int for blue value (0-255)
    int spinSpeed = Serial.parseInt();  //speed for spin weapon (0-6)

    if (Serial.read() == '\n') {  //newline defines end of transmission
      setLEDColour(redVal, greenVal, blueVal);
    }
  }
}
