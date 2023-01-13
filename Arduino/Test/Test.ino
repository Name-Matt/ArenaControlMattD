void setup() {
  // Initialize serial communication at 9600 baud
  Serial.begin(9600);
}

void loop() {
  // Read the value of pin A0
  int sensorValue = analogRead(A0);
  // Send the value over serial
  Serial.println("Connected to Arena");
  // Wait for a bit before reading the next value
  delay(100);
}
