// Example by Tom Igoe

import processing.serial.*;

int lf = 10;    // Linefeed in ASCII
String myString = null;
Serial myPort;  // The serial port

void setup() {
  size(800,600);
  // List all the available serial ports
  println(Serial.list());
  // Open the port you are using at the rate you want:
  myPort = new Serial(this, "/dev/tty.usbmodem411", 9600);
  myPort.clear();
  // Throw out the first reading, in case we started reading 
  // in the middle of a string from the sender.
  myString = myPort.readStringUntil(lf);
  myString = null;
}

void draw() {
  while (myPort.available() > 0) {
    myString = myPort.readStringUntil(lf);
    if (myString != null) {
      
      println(myString);
      background(255);
      fill(float(myString),100,100);
      if (float(myString) > 100) {
      ellipse(width/2, height/2, float(myString)*2, float(myString)*2);
      } else {
      rect(0, 100, float(myString)*4, 120); 
      }
    }
  }
}
