/*
 * The following program is to be implemented on the Servo Control Unit of SDR's
 * Liquids Avionics Circuit
 * 
 * The following program controls the servo position of the propellant ball valves
 * via the Serial input. The Python GUI accesses this program via the 
 * bunker control Serial Monitor.
 * 
 * The unit which this code is uploaded onto must maintain a serial connection
 * with the Bunker control unit at all times. If connection is interrupted,
 * there will be a loss of servo control.
 * 
 * Author: Nitish Chennoju
*/

#include <Servo.h> // general PWM servo library

#define NUM_SERVOS 2

const int SERVO_PINS[] = {7, 10}; // keeps track of servo pins
Servo s[NUM_SERVOS]; // array of servo objects

int s_pos; // temporary variable to set servo position

// logs serial messages sent to controller
String msg = ""; // consists of servo # and position (0,100)


void setup() {
  Serial.begin(115200); // begins Serial Monitor for dubugging

  //attach servo objects to specified pin #s
  for(int i = 0; i < sizeof(s); i++) {
    s[i].attach(SERVO_PINS[i]);
  }
}

void loop() {
  msg = ""; // resets serial communication msg var

  while(Serial.available() > 0){
    //READ SERIAL MONITOR BY CHAR
    
    msg += char(Serial.read());  //.read() is non-blocking function (minimal delay)
    delayMicroseconds(100); //DO NOT DELETE THIS DELAY
  }
  
  if(msg != ""){ // if message recieved

    //assumed that msg contains 3 characters (exceptions handled by bunker control unit)
    /*
     * MSG CONTENTS -> msg[0], msg[1], msg[2]
     * 
     * msg[0] = 'S' in all cases
     * msg[1] = 0 or 1 (servo s1 or s2), since NUM_SERVOS is 2
     * msg[2] = char int (0-100) for servo position
    */

    // Index out of bounds handling for # of servos
    if(int(msg[1])-48 < NUM_SERVOS){
      s_pos = map(int(msg[2]), 0, 100, 0, 180); // hobby servo require parameters [0,180]
                                                // while serial input is [0, 100]
      s[int(msg[1])-48].write(s_pos);
    }else{
      Serial.println("ERROR: Servo#" + String(int(msg[1])-48) + " does not exist"); // FOR TEST
    }
    
    Serial.println(msg + " RECIEVED"); // FOR TEST
  }
}
