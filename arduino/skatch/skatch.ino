#include <Servo.h>

#define MAX_X  180
#define MIN_X 0

#define MAX_Y 180
#define MIN_Y 0
Servo Sx;
Servo Sy;
int x = 110, y = 90;
int command_x = 0, command_y =0;

void update(int x, int y){
  
  Sx.write(x);
  Sy.write(y);
}

void setup() {
  Serial.begin(9600);
  Sx.attach(2);
  Sy.attach(3);
  update(x, y);
}

void loop() {
  //принять команду
  while(Serial.available() > 0) {
    command_x = Serial.parseInt();
    command_y = Serial.parseInt();
  }
  //если commnad_x
  if (command_x == -1) {
      x--;
  } else if (command_x == 1) {
      x++;
  } else if (command_x == 0) {
      
  }
  
  //если commnad_x
  if (command_y == -1) {
      y++;
  } else if (command_y == 1) {
      y--;
  } else if (command_y == 0) {
      
  }
  
  update(x, y);
  delay(150);  
}

