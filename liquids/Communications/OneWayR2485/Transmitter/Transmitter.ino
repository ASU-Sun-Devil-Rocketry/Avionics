// RS-485 Communications Test
// One Way Communication
// Transmiter Script
// Read Potentiometer Reading
// Send Reading to Receiver

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
  Serial.begin(9600,SERIAL_8O2);

  // Declare Pin Modes 
  pinMode(potPin,INPUT);
  pinMode(enablePin, OUTPUT);

   // Enable Writing to RS-485 Converter
  digitalWrite(enablePin,writeEnable);

}

void loop() {
  
  // Read Pot Pin Voltage
  potVal = analogRead(potPin);

  // Print Data to Serial Interface
  Serial.print('<');
  Serial.print(potVal);
  Serial.print('>');

  // Delay For Stability
  delay(100);
}
