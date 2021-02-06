#include<Wire.h>

void setup() {
  // put your setup code here, to run once:
  Wire.begin();
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:

  Wire.requestFrom(8,4);
  String dataString;
  char c;
  
  while(Wire.available()){
   
    char c = Wire.read();
    dataString = dataString +c;     
    }
    
    Serial.println(dataString);

  delay(500);

}
