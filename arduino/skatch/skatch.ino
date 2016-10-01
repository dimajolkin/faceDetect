#include <Servo.h>

Servo Sx;
Servo Sy;
int x = 0, y =0;
void setup() {
  Serial.begin(9600);
  Sx.attach(2);
  Sy.attach(3);
}

void update(int x, int y){
  Sx.write(x);
  Sy.write(y);
}
void loop() {
  while(Serial.available() > 0) {
    x = Serial.parseInt();
    y = Serial.parseInt();
    if (Serial.find("+")) {
       update(x + 110, y + 100);
       Serial.write("x:");
       Serial.write(x);
       Serial.write(";y:");
       Serial.write(y);
    }
  }
}

