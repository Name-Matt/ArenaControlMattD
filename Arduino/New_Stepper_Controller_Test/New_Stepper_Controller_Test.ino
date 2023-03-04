// Define pins for TB6600 driver
const int EN = 10;   // Enable pin
const int DIR = 11;  // Direction pin
const int PUL = 12; // Pulse pin

// Set motor speed and steps per revolution
const int motorSpeed = 1000;
const int stepsPerRevolution = 800;

void setup() {
  // Set up the pins as outputs
  pinMode(EN, OUTPUT);
  pinMode(DIR, OUTPUT);
  pinMode(PUL, OUTPUT);

  // Set the initial pin states
  digitalWrite(EN, LOW);
  digitalWrite(DIR, LOW);
  digitalWrite(PUL, LOW);
}

void loop() {
  // Enable the motor driver
  digitalWrite(EN, HIGH);

  // Set the direction of the motor (HIGH = clockwise, LOW = counterclockwise)
  digitalWrite(DIR, HIGH);

  // Move the motor one revolution
  for (int i = 0; i < stepsPerRevolution; i++) {
    digitalWrite(PUL, HIGH);
    delayMicroseconds(motorSpeed);
    digitalWrite(PUL, LOW);
    delayMicroseconds(motorSpeed);
  }

  // Disable the motor driver
  digitalWrite(EN, LOW);

  // Wait a second before reversing direction
  delay(1000);

  // Enable the motor driver
  digitalWrite(EN, HIGH);

  // Set the direction of the motor (HIGH = clockwise, LOW = counterclockwise)
  digitalWrite(DIR, LOW);

  // Move the motor one revolution
  for (int i = 0; i < stepsPerRevolution; i++) {
    digitalWrite(PUL, HIGH);
    delayMicroseconds(motorSpeed);
    digitalWrite(PUL, LOW);
    delayMicroseconds(motorSpeed);
  }

  // Disable the motor driver
  digitalWrite(EN, LOW);

  // Wait a second before repeating the loop
  delay(1000);
}

