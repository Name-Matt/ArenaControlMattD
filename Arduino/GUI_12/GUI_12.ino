int SpinPins[6] = { 4, 5, 6, 7, 8, 12 };           //the pins used for spinning motor
int SpinPinsLen = sizeof(SpinPins) / sizeof(int);  //length of the array holding the pins
int LEDpins[3] = { 9, 10, 11 };                    //pins used for LED control (RGB) - MUST BE PWM PINS
int LEDpinsLen = sizeof(LEDpins) / sizeof(int);
int DoorPins[2] = { 2, 3 };  //pins used for door sensors - MUST BE INTERRUPT PINS
int DoorPinsLen = sizeof(DoorPins) / sizeof(int);


int pin4State = 0;
int pin5State = 0;
int pin6State = 0;
int pin7State = 0;
int pin8State = 0;
int pin12State = 0;

bool doorOpen = true;  //boolean to hold if door open or closed
bool emrgStop = false;  //true if emergenct stop pressed

int redState = 0;
int greenState = 255;
int blueState = 200;

String serialInfo = "Test";

void setup() {
  Serial.begin(9600);

  //decide if the doors are open or closed at start
  if ((digitalRead(DoorPins[0]) == LOW) && (digitalRead(DoorPins[1]) == LOW)) {
    doorOpen = false;
    serialInfo = "DOOR CLOSE @ START";
    Serial.println(serialInfo);
  } else {
    doorOpen = true;
    serialInfo = "DOOR OPEN @ START";
    Serial.println(serialInfo);
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
    attachInterrupt(digitalPinToInterrupt(DoorPins[i]), doorOPENED_ISR, FALLING);
  }

  setLEDColour(255, 0, 40);  //sets lights pink to start
  // Send the value over serial
  serialInfo = "Connected to Arena";
  Serial.println(serialInfo);
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

void doorOPENED_ISR() {  //what to do if door is open
  doorOpen = true;
  serialInfo = "DOOR OPENED - EMERGENCY STOP";
  Serial.println(serialInfo);
  setLEDColour(255, 0, 0);  //set lights red
  //keep running this loop if ANY doors are open
  while (doorOpen == true) {
    //will break the while loop if the door is shut
    if ((digitalRead(DoorPins[0]) == LOW) && digitalRead(DoorPins[1]) == LOW) {
      doorOpen = false;
      serialInfo = "DOOR SHUT - RESUME";
      Serial.println(serialInfo);
    }
    //delay to prevent saturating the serial line
    delay(100);
  }
  setLEDColour(redState, greenState, blueState);
}



void loop() {
  // Check for incoming data
  if (Serial.available() > 0) {
    // Read incoming data
    char inByte = Serial.read();

    // Emergency stop command
    if (inByte == 'E') {
      digitalWrite(SpinPins[0], LOW);
      digitalWrite(SpinPins[1], LOW);
      digitalWrite(SpinPins[2], LOW);
      digitalWrite(SpinPins[3], LOW);
      digitalWrite(SpinPins[4], LOW);
      digitalWrite(SpinPins[5], LOW);
      setLEDColour(255,0,0);
      serialInfo = "EMERGENCY STOP ACTIVATED";
      Serial.println(serialInfo);
    }
    // Resume commmand
    else if (inByte == 'R') {
      digitalWrite(SpinPins[0], pin4State);
      digitalWrite(SpinPins[1], pin5State);
      digitalWrite(SpinPins[2], pin6State);
      digitalWrite(SpinPins[3], pin7State);
      digitalWrite(SpinPins[4], pin8State);
      digitalWrite(SpinPins[5], pin12State);
      setLEDColour(redState,greenState,blueState);
      serialInfo = "Game Resume";
      Serial.println(serialInfo);
    }
    // Pin 4 command
    else if (inByte == '0') {
      digitalWrite(SpinPins[0], HIGH);
      digitalWrite(SpinPins[1], LOW);
      digitalWrite(SpinPins[2], LOW);
      digitalWrite(SpinPins[3], LOW);
      digitalWrite(SpinPins[4], LOW);
      digitalWrite(SpinPins[5], LOW);
      serialInfo = "Spin Speed 0%";
      Serial.println(serialInfo);

      pin4State = 1;
      pin5State = 0;
      pin6State = 0;
      pin7State = 0;
      pin8State = 0;
      pin12State = 0;

    }
    // Pin 5 command
    else if (inByte == '1') {
      digitalWrite(SpinPins[0], LOW);
      digitalWrite(SpinPins[1], HIGH);
      digitalWrite(SpinPins[2], LOW);
      digitalWrite(SpinPins[3], LOW);
      digitalWrite(SpinPins[4], LOW);
      digitalWrite(SpinPins[5], LOW);
      serialInfo = "Spin Speed 20%";
      Serial.println(serialInfo);

      pin4State = 0;
      pin5State = 1;
      pin6State = 0;
      pin7State = 0;
      pin8State = 0;
      pin12State = 0;
    }
    // Pin 6 command
    else if (inByte == '2') {
      digitalWrite(SpinPins[0], LOW);
      digitalWrite(SpinPins[1], LOW);
      digitalWrite(SpinPins[2], HIGH);
      digitalWrite(SpinPins[3], LOW);
      digitalWrite(SpinPins[4], LOW);
      digitalWrite(SpinPins[5], LOW);
      serialInfo = "Spin Speed 40%";
      Serial.println(serialInfo);

      pin4State = 0;
      pin5State = 0;
      pin6State = 1;
      pin7State = 0;
      pin8State = 0;
      pin12State = 0;
    }
    // Pin 7 command
    else if (inByte == '3') {
      digitalWrite(SpinPins[0], LOW);
      digitalWrite(SpinPins[1], LOW);
      digitalWrite(SpinPins[2], LOW);
      digitalWrite(SpinPins[3], HIGH);
      digitalWrite(SpinPins[4], LOW);
      digitalWrite(SpinPins[5], LOW);
      serialInfo = "Spin Speed 60%";
      Serial.println(serialInfo);

      pin4State = 0;
      pin5State = 0;
      pin6State = 0;
      pin7State = 1;
      pin8State = 0;
      pin12State = 0;
    }
    // Pin 8 command
    else if (inByte == '4') {
      digitalWrite(SpinPins[0], LOW);
      digitalWrite(SpinPins[1], LOW);
      digitalWrite(SpinPins[2], LOW);
      digitalWrite(SpinPins[3], LOW);
      digitalWrite(SpinPins[4], HIGH);
      digitalWrite(SpinPins[5], LOW);
      serialInfo = "Spin Speed 80%";
      Serial.println(serialInfo);

      pin4State = 0;
      pin5State = 0;
      pin6State = 0;
      pin7State = 0;
      pin8State = 1;
      pin12State = 0;
    }
    // Pin 12 command
    else if (inByte == '5') {
      digitalWrite(SpinPins[0], LOW);
      digitalWrite(SpinPins[1], LOW);
      digitalWrite(SpinPins[2], LOW);
      digitalWrite(SpinPins[3], LOW);
      digitalWrite(SpinPins[4], LOW);
      digitalWrite(SpinPins[5], HIGH);
      serialInfo = "Spin Speed 100%";
      Serial.println(serialInfo);

      pin4State = 0;
      pin5State = 0;
      pin6State = 0;
      pin7State = 0;
      pin8State = 0;
      pin12State = 1;
    }
    // Corner Trap Enable
    else if (inByte == 'C') {
      serialInfo = "Corner Trap Enabled";
      Serial.println(serialInfo);
    }
    // Corner Trap Disable
    else if (inByte == 'D') {
      serialInfo = "Corner Trap Disabled";
      Serial.println(serialInfo);
    }
    // Game Mode 1
    else if (inByte == 'M') {
      serialInfo = "Game Mode 1";
      Serial.println(serialInfo);
    }
        // Game Mode 2
    else if (inByte == 'N') {
      serialInfo = "Game Mode 2";
      Serial.println(serialInfo);
    }
        // Game Mode 3
    else if (inByte == 'O') {
      serialInfo = "Game Mode 3";
      Serial.println(serialInfo);
    }
        // Game Mode 4
    else if (inByte == 'P') {
      serialInfo = "Game Mode 4";
      Serial.println(serialInfo);
    }
        // Game Mode 5
    else if (inByte == 'Q') {
      serialInfo = "Game Mode 5";
      Serial.println(serialInfo);
    }
  }
}
