#include <Servo.h>

Servo s1;

int degree_start = 0;       // Start of the range in degrees
int degree_end = 360;       // End of the range in degrees
int pin = 14;               // Pin 14 is Analog 0
int dly = 125;              // Delay between loop iterations

void setup() {
  pinMode(pin, OUTPUT);
  s1.attach(pin);           // Analog 0

  Serial.begin(19200);
  Serial.println("Maker's Digest: Ready");
}

void loop() {
  int i = 0;
  Serial.println("This is zero.");
  
  s1.write(i);
  delay(1000);
  
  for(i = degree_start; i <= degree_end; i++) {
    s1.write(i);
    Serial.println(i);
    delay(dly);
  }

  Serial.println("Done with test");
  delay(2000);
}
