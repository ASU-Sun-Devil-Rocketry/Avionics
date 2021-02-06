// RS-485 Communications Test
// Two Way Communication
// Sender Script
// Read Potentiometer Reading
// Send Reading to Receiver
// Wait For Response
// Print Response to Serial Monitor

// Library for Multiple Serial Ports
#include <SoftwareSerial.h>

// Software Serial Rx and TX pins
const int RS_485rx = 6;
const int RS_485tx = 7;

// Instantiate RS-485 Serial Port Object
SoftwareSerial RS_485(RS_485rx,RS_485tx);

// Memory reserved for incoming Data
const byte numChars = 8; // 32 byte buffer size
char receivedChars[8]; // Declare Buffer

// Variable to indicate new data to be read
boolean newData = false;

// Potentiometer Pin
const int potPin = A0;

// Potentiometer Reading
uint16_t potVal = 0;

// RS-485 Converter Pins
const int enablePin = 2;
const bool readEnable = LOW;
const bool writeEnable = HIGH;

void setup() {
  // Start Serial Interface
  Serial.begin(9600);
  RS_485.begin(9600);
  
  // Declare Pin Modes 
  pinMode(potPin,INPUT);
  pinMode(enablePin, OUTPUT);

}

void loop() {
  
  // Read Pot Pin Voltage
  potVal = analogRead(potPin);

  // Write Potentiometer value to Serial Interface
  sendData(potVal);

  // Read Data From Serial Monitor
  receiveData();

  // Print Recieved Data to Serial Monitor
  showData();

  // Delay For Stability
  delay(100);

}

// Function to send data to serial interface
void sendData(int val){

  // Enable RS-485 converter to write data to bus
  // Print Data to Serial Interface
  digitalWrite(enablePin, writeEnable);
  RS_485.print('<');
  RS_485.print(val);
  RS_485.print('>');
  
  }

// Function to call to obtain Data
void receiveData(){

   // Variable to indicate that data is being recieved
   static boolean inProgress = false;

   // Counter Variable
   static byte n = 0;

   // Start and End Markers
   char startMarker = '<';
   char endMarker = '>';

   // Variable to store each char read
   char c;

   // Enable RS-485 Module to read data
   digitalWrite(enablePin, readEnable);

   // Read Serial Port While there is data available
   while(RS_485.available()>0 && newData == false){
    
       // Read Character From Serial Port
       c = RS_485.read();

       // Add Character to array if data is being read
       if(inProgress == true){
        // Don't Add Char if it is the endmarker
        if (c != endMarker){
          receivedChars[n] = c;
          n++;

          // Prevent Buffer Overflow
         if (n >= numChars){
          n = numChars -1;
          }
        }
        else {
          
          receivedChars[n] = '\0'; // End string 
          inProgress = false;
          n = 0; // Reset Counter
          newData = true; // Indicate that next data point can be read
          
          }
        
        } else if(c == startMarker){
          inProgress = true;
          }  
       
    }  
  }

  void showData(){
    if (newData == true){
      Serial.print("Data Recieved: ");
      Serial.println(receivedChars);
      newData = false;
      }
    }
