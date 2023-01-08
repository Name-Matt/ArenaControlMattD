const int pin4 = 4;
const int pin5 = 5;
const int pin6 = 6;
const int pin7 = 7;
const int pin8 = 8;
const int pin12 = 12;

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
    // Pin 4 command
    else if (inByte == '4') {
      digitalWrite(pin4, HIGH);
      digitalWrite(pin5, LOW);
      digitalWrite(pin6, LOW);
      digitalWrite(pin7, LOW);
      digitalWrite(pin8, LOW);
      digitalWrite(pin12, LOW);

    }
    // Pin 5 command
    else if (inByte == '5') {
      digitalWrite(pin4, LOW);
      digitalWrite(pin5, HIGH);
      digitalWrite(pin6, LOW);
      digitalWrite(pin7, LOW);
      digitalWrite(pin8, LOW);
      digitalWrite(pin12, LOW);
    }
    // Pin 6 command
    else if (inByte == '6') {
      digitalWrite(pin4, LOW);
      digitalWrite(pin5, LOW);
      digitalWrite(pin6, HIGH);
      digitalWrite(pin7, LOW);
      digitalWrite(pin8, LOW);
      digitalWrite(pin12, LOW);
    }
    // Pin 7 command
    else if (inByte == '7') {
      digitalWrite(pin4, LOW);
      digitalWrite(pin5, LOW);
      digitalWrite(pin6, LOW);
      digitalWrite(pin7, HIGH);
      digitalWrite(pin8, LOW);
      digitalWrite(pin12, LOW);
    }
    // Pin 8 command
    else if (inByte == '8') {
      digitalWrite(pin4, LOW);
      digitalWrite(pin5, LOW);
      digitalWrite(pin6, LOW);
      digitalWrite(pin7, LOW);
      digitalWrite(pin8, HIGH);
      digitalWrite(pin12, LOW);
    }
    // Pin 12 command
    else if (inByte == '2') {
      digitalWrite(pin4, LOW);
      digitalWrite(pin5, LOW);
      digitalWrite(pin6, LOW);
      digitalWrite(pin7, LOW);
      digitalWrite(pin8, LOW);
      digitalWrite(pin12, HIGH);
    }
  }
}
