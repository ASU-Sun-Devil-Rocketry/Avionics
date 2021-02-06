// RS-485 Communications Test
// One Way Communication
// Reciever Script
// Read Incoming Data from Transceiver
// Print Data To Serial Port

// Memory reserved for incoming Data
const byte numChars = 8; // 32 byte buffer size
char receivedChars[8]; // Declare Buffer

// Variable to indicate new data to be read
boolean newData = false;

// Variable for Storing Transmitted Data
int recievedVal = 0;

// RS-485 Converter Pins
const int enablePin = 2;
const bool readEnable = LOW;
const bool writeEnable = HIGH;

void setup() {
  // Begin Serial Communications
  Serial.begin(9600, SERIAL_8O2);

  // Set Pin Modes
  pinMode(enablePin, OUTPUT);

  // Set Write Enable to LOW since reciever won't be writing any data
  digitalWrite(enablePin, readEnable);
}

void loop() {

  // Recieve Data String from Serial Port
  receiveData();

  // Print Data to the Serial Monitor
  showData();

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

   // Read Serial Port While there is data available
   while(Serial.available()>0 && newData == false){
    
       // Read Character From Serial Port
       c = Serial.read();

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
