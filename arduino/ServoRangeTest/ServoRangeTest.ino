#include <Servo.h>

Servo servo1;

void setup() {
  pinMode(1, OUTPUT);
  servo1.attach(14); // Analog 0

  Serial.begin(19200);
  Serial.println("Maker's Digest: Ready");
}

void loop() {
  int i = 0;

  Serial.println("This is zero.");
  servo1.write(i);
  delay(1000);
  for(i = 0; i <= 200; i++) {
    servo1.write(i);
    Serial.println(i);
    delay(125);
  }

  Serial.println("Done with test");
  delay(1000);
}
