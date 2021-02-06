// RS-485 Communications Test
// Reciever Script
// Read Incoming Data from Transceiver
// Light Up onboard LED accordingly

const int ledPin = 6;

int incomingByte = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(ledPin,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    
    incomingByte = Serial.read();

    //Serial.write(incomingByte);

    //digitalWrite(ledPin,HIGH);

    if (incomingByte == 'H'){
      
      digitalWrite(ledPin, HIGH);
      }
    else if (incomingByte == 'L'){
      
      digitalWrite(ledPin, LOW);
      }
    else{
      
      Serial.write("Invalid Input");
      }
    
    
    }
}
