
int SpinPins[6] = { 4, 5, 6, 7, 8, 12 };           //the pins used for spinning motor
int SpinPinsLen = sizeof(SpinPins) / sizeof(int);  //length of the array holding the pins
int LEDpins[3] = { 9, 10, 11 };                    //pins used for LED control - MUST BE PWM PINS
int LEDpinsLen = sizeof(LEDpins) / sizeof(int);
int DoorPins[2] = { 2, 3 };  //pins used for door sensors - MUST BE INTERRUPT PINS
int DoorPinsLen = sizeof(DoorPins) / sizeof(int);

bool doorOpen = true;


void setup() {
  Serial.begin(19200);

  if (digitalRead(DoorPins[1]) == LOW) {
    doorOpen = false;
    Serial.println("DOOR CLOSE");
  } else {
    doorOpen = true;
    Serial.println("DOOR OPEN");
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
}

void doorOPENED() {  //what to do if door is open
  doorOpen = true;

  while (doorOpen == true) {
    if (digitalRead(DoorPins[1]) == LOW) {
      doorOpen = false;
      Serial.println("DOOR CLOSED");
    }
    else{
      Serial.println("STILL OPEN");
    }
    delay(100);
  }
}


void loop() {
  // put your main code here, to run repeatedly.
  if (doorOpen == true){
    doorOPENED();
  }
}
