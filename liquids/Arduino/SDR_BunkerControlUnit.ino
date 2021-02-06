/*
 * The following program is to be implemented on the Bunker Control Unit of SDR's
 * Liquids Avionics Circuit
 * 
 * The following program controls relay outputs + servo position via the Serial
 * monitor. The Python GUI accesses the Serial Monitor via the pyserial module.
 * Thus, full actuator control is obtained through this program.
 * 
 * Author: Nitish Chennoju
*/

#include <SoftwareSerial.h>

SoftwareSerial ser(2, 3); // RX, TX
const int relayPins[] = {12, 11, 10, 9, 8, 7};

char in;
int i;
int num;

void setup() {
  
  //Initialize Serial Monitor
  Serial.begin(115200);
  Serial.println("BEGIN");  //Sample MSG

  //Initialize Serial Communication between boards
  ser.begin(115200);

  //Declare relay pins as OUTPUTS
  for (int i = 0; i < sizeof(relayPins); i++) {
    pinMode(relayPins[i], OUTPUT);
  }
  
}

void loop() {
  
  //reset vars for Serial monitor input (done via aggregation of chars)
  i = 0;
  char msg[32] = "";
  
  while(Serial.available() > 0) {
      //READ SERIAL MONITOR CHAR
      in = Serial.read(); //.read() is non-blocking function (minimal delay)
      
      //Serial.println(String(int(in)) + String(msg));  //FOR TEST
      
      delayMicroseconds(100); //DO NOT DELETE THIS DELAY
      if(int(in) == 10){  //if newline, break loop
        break;
      }
      msg[i] = in;
      i++;
  }

  /* -- RELAY CONTROL MODE --
   * Relay trigger format
   * [relayPins[#]][relay # state] i.e. 00 -> relayPins[0] OFF
   */
  if(isDigit(msg[0]) && isDigit(msg[1])){
    if(int(msg[1])-48 == 1){
      digitalWrite(relayPins[int(msg[0])-48], HIGH);      
    }else{
      digitalWrite(relayPins[int(msg[0])-48], LOW);
    }
    //Serial.println(int(msg[0])-48);  //FOR TEST
    //Serial.println(int(msg[1])-48);  //FOR TEST
  }

  /* -- SERVO CONTROL MODE --
   * Servo trigger format
   * S[servoPin[#]][servo position # (from 0 - 100)] i.e. S02 -> servo[0] to pos 90
   * 0 to 0deg, 100 to 180 deg
   */
  if(msg[0] == 'S' && isDigit(msg[1]) && int(msg[2]) <= 100){
    //Send Data to Servo/Actuator Controller
    Serial.print(F("Set Servo#"));
    Serial.print(int(msg[1])-48);
    Serial.print(F(" pos to "));
    Serial.println(int(msg[2]));

    //Serial write data via ser software serial
    ser.println(msg);
  }
  
}
