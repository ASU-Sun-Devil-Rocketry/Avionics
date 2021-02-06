// Read Pot Adjustable Analog Voltage
// Use External voltage source
// Wire Potentiomenter to potPin

const int potPin = A0;

void setup() {

  // Initiate serial Communications
  Serial.begin(9600);

}

// Code Start
void loop() {

  // Read Pot Value
  int val = analogRead(potPin);
  
  // Display Voltage in serial monitor
  Serial.println(val);

  // Delay for stability
  delay(1);

}
