# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 16:08:50 2022
This is prepared to test servo slider controlled over serial port.

This code send data through serial port to a ATmega328 or ATmega32u4 board
to controll a servo connected. 

The firmware in arduino pool for serial data, once a string start with 
a "P" and end with a "\n" and numbers in between. 

@author: Dapeng
"""
import time
# import random
from serial import Serial
ser = Serial('/dev/ttyACM0', 115200, timeout = 0.5)
move_interval = 1
for i in range(10):
    ser.write(bytes('P40\n', 'ascii'))
    time.sleep(move_interval)
    ser.write(bytes('P140\n', 'ascii'))
    time.sleep(move_interval)
# for i in range(10):
#     cmd = motor_1+str(200 + 30 * i)+'\n'
#     ser.write(bytes(cmd, 'ascii'))
#     time.sleep(send_interval_2)
#     cmd = motor_2+str(50 * i)+'\n'
#     ser.write(bytes(cmd, 'ascii'))
#     time.sleep(move_interval_2)
ser.close()

"""
// The Arduino Code to cooperate with the above code 
#include <Servo.h>
# define BUFFER_SIZE 100

Servo servo;
char buf[BUFFER_SIZE];
// initalize a string to recieve serial data
String rec_string = ""; 
void setup()
{
  servo.attach(9);  //The Tilt servo is attached to pin 9.
  servo.write(90);
  Serial.begin(9600);  //Set up a serial connection for 57600 bps.
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
}
void loop(){

  
  // check if serial data is available
  if(Serial.available() > 0){
    int rlen = Serial.readBytesUntil('\n', buf, BUFFER_SIZE);
    if (buf[0] == 'P'){
      for (int i = 1; i < rlen; i++)
        rec_string += buf[i];
      int pos = rec_string.toInt();
      //String message = "motor goes to " + rec_string;
      //Serial.println(message);
      servo.write(pos);
      rec_string = "";
    }
    
  }
}
"""