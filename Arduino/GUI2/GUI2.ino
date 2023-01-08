"""
Created on Sun Jan  8 20:09:33 2023

@author: Matt
"""

const int pin4 = 4;
const int pin5 = 5;
const int pin6 = 6;
const int pin7 = 7;
const int pin8 = 8;
const int pin12 = 12;

int pin4State = 0;
int pin5State = 0;
int pin6State = 0;
int pin7State = 0;
int pin8State = 0;
int pin12State = 0;

void setup() {
  // Set all pins as output
  pinMode(pin4, OUTPUT);
  pinMode(pin5, OUTPUT);
  pinMode(pin6, OUTPUT);
  pinMode(pin7, OUTPUT);
  pinMode(pin8, OUTPUT);
  pinMode(pin12, OUTPUT);

  // Set all pins to low (off)
  digitalWrite(pin4, LOW);
  digitalWrite(pin5, LOW);
  digitalWrite(pin6, LOW);
  digitalWrite(pin7, LOW);
  digitalWrite(pin8, LOW);
  digitalWrite(pin12, LOW);

  // Set up serial communication
  Serial.begin(9600);
}

void loop() {
  // Check for incoming data
  if (Serial.available() > 0) {
    // Read incoming data
    char inByte = Serial.read();

    // Emergency stop command
    if (inByte == 'E') {
      digitalWrite(pin4, LOW);
      digitalWrite(pin5, LOW);
      digitalWrite(pin6, LOW);
      digitalWrite(pin7, LOW);
      digitalWrite(pin8, LOW);
      digitalWrite(pin12, LOW);
    }
    // Resume commmand
    else if (inByte == 'R') {
      digitalWrite(pin4, pin4State);
      digitalWrite(pin5, pin5State);
      digitalWrite(pin6, pin6State);
      digitalWrite(pin7, pin7State);
      digitalWrite(pin8, pin8State);
      digitalWrite(pin12, pin12State);
    }
    // Pin 4 command
    else if (inByte == '4') {
      digitalWrite(pin4, HIGH);
      digitalWrite(pin5, LOW);
      digitalWrite(pin6, LOW);
      digitalWrite(pin7, LOW);
      digitalWrite(pin8, LOW);
      digitalWrite(pin12, LOW);

      pin4State = 1;
      pin5State = 0;
      pin6State = 0;
      pin7State = 0;
      pin8State = 0;
      pin12State = 0;

    }
    // Pin 5 command
    else if (inByte == '5') {
      digitalWrite(pin4, LOW);
      digitalWrite(pin5, HIGH);
      digitalWrite(pin6, LOW);
      digitalWrite(pin7, LOW);
      digitalWrite(pin8, LOW);
      digitalWrite(pin12, LOW);

      pin4State = 0;
      pin5State = 1;
      pin6State = 0;
      pin7State = 0;
      pin8State = 0;
      pin12State = 0;
    }
    // Pin 6 command
    else if (inByte == '6') {
      digitalWrite(pin4, LOW);
      digitalWrite(pin5, LOW);
      digitalWrite(pin6, HIGH);
      digitalWrite(pin7, LOW);
      digitalWrite(pin8, LOW);
      digitalWrite(pin12, LOW);

      pin4State = 0;
      pin5State = 0;
      pin6State = 1;
      pin7State = 0;
      pin8State = 0;
      pin12State = 0;
    }
    // Pin 7 command
    else if (inByte == '7') {
      digitalWrite(pin4, LOW);
      digitalWrite(pin5, LOW);
      digitalWrite(pin6, LOW);
      digitalWrite(pin7, HIGH);
      digitalWrite(pin8, LOW);
      digitalWrite(pin12, LOW);

      pin4State = 0;
      pin5State = 0;
      pin6State = 0;
      pin7State = 1;
      pin8State = 0;
      pin12State = 0;
    }
    // Pin 8 command
    else if (inByte == '8') {
      digitalWrite(pin4, LOW);
      digitalWrite(pin5, LOW);
      digitalWrite(pin6, LOW);
      digitalWrite(pin7, LOW);
      digitalWrite(pin8, HIGH);
      digitalWrite(pin12, LOW);

      pin4State = 0;
      pin5State = 0;
      pin6State = 0;
      pin7State = 0;
      pin8State = 1;
      pin12State = 0;
    }
    // Pin 12 command
    else if (inByte == '2') {
      digitalWrite(pin4, LOW);
      digitalWrite(pin5, LOW);
      digitalWrite(pin6, LOW);
      digitalWrite(pin7, LOW);
      digitalWrite(pin8, LOW);
      digitalWrite(pin12, HIGH);

      pin4State = 0;
      pin5State = 0;
      pin6State = 0;
      pin7State = 0;
      pin8State = 0;
      pin12State = 1;
    }
  }
}
