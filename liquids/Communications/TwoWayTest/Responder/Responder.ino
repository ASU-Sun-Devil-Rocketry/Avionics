// RS-485 Communications Test
// Two Way Communication
// Responder Script
// Read Incoming Data from Transceiver
// Convert Integer to float voltage
// Send Voltage back to sender

// Library For RS-485 Serial Port
#include <SoftwareSerial.h>

// Software Serial RX and TX pins
const int RS_485rx = 6;
const int RS_485tx = 7;

// Instantiate Serial Port Object
SoftwareSerial RS_485(RS_485rx,RS_485tx);

// Memory reserved for incoming Data
const byte numChars = 8; // 32 byte buffer size
char receivedChars[8]; // Declare Buffer

// Variable to indicate new data to be read
boolean newData = false;

// Variable for Storing Transmitted Data
int receivedVal = 0;

// Variable For Storing Voltage
float voltage = 0.0;

// RS-485 Converter Pins
const int enablePin = 2;
const bool readEnable = LOW;
const bool writeEnable = HIGH;

void setup() {
  // Begin Serial Communications
  Serial.begin(9600);
  RS_485.begin(9600);

  // Set Pin Modes
  pinMode(enablePin, OUTPUT);

}

void loop() {

  // Recieve Data String from Serial Port
  receiveData();

  // Send a Response
  respond();

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

   // Enable Reading from the RS-485 Module
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

  int respond(){
    if (newData == true){
      receivedVal = atoi(receivedChars);
      voltage = float(receivedVal*5.0/1023);
      digitalWrite(enablePin, writeEnable); // Enable Writing
      RS_485.print("<");
      RS_485.print(voltage);
      RS_485.print(">");
      //Serial.print("Data Recieved: ");
      //Serial.println(receivedChars);
      //Serial.print("Data Changed to: ");
      //Serial.println(voltage);
      newData = false;
      }

    }
