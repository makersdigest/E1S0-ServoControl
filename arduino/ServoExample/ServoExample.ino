
/*
 * Servo Example
 * Maker's Digest
 */
#include <Servo.h>

Servo s1;             // Instantiate Servo Object

int pin = 14;         // Pin 14 is Analog 0
int dly = 500;        // Set Delay to 500ms. Change this to change the speed

void setup() {
  pinMode(pin, OUTPUT);
  s1.attach(pin);    // Attach to Analog 0

  Serial.begin(19200);
  Serial.println("Maker's Digest: Ready");
}

void loop() {
  s1.write(0);      // Set position 0 degrees
  delay(dly);
  
  s1.write(90);     // Set Position 90 degrees
  delay(dly);
  
  s1.write(180);    // Set Position 180 degrees
  delay(dly);
  
  s1.write(90);     // Set Position 90 degrees
  delay(dly);    
}
