// RS-485 Communications Test
// Transmiter Script
// Send Data to Receiver Module


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.write("H");
  delay(1000);
  Serial.write("L");
  delay(1000);
}
