const int limitSwitchPin = 2;
const int debounceDelay = 50;

bool switchState;
bool lastSwitchState = LOW;
unsigned long lastDebounceTime = 0;

void setup() {
  pinMode(limitSwitchPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(limitSwitchPin), test, FALLING);
  Serial.begin(9600);
}

void loop() {
  // other code here
  delay(100);
}

void test() {
  int reading = digitalRead(limitSwitchPin);
  Serial.println("TEST");

  if (reading != lastSwitchState) {
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {
    if (reading != switchState) {
      switchState = reading;

      if (switchState == LOW) {
        // limit switch triggered event
        Serial.println("Limit switch triggered!");
      }
    }
  }

  lastSwitchState = reading;
}
