// Define variables for the recorded times of continuity loss
// Make variable volatile to prevent compiler from prematurely assigning the times values 
volatile unsigned long t1, t2;
double t1_dec, t2_dec, burnTime;

// Define the Continuity Check pins 
const int cont_pin1 = 2;
const int cont_pin2 = 3;

// Initial time of event loop 
int startTime;

// Current Time 
unsigned long currentTime;

// Identifier Variable for determining when to print to the serial monitor
bool results_ready = 0;

void setup() {

   // Initialize the serial monitor
   Serial.begin(9600);

   // Initialize Interrupt Pins
   // Interrupts are trigered when voltage falls from high to low
   attachInterrupt(digitalPinToInterrupt(cont_pin1), record1, FALLING);
   attachInterrupt(digitalPinToInterrupt(cont_pin2), record2, FALLING);

   // Delay for a few seconds 
   delay(3000);

   // Print a Start Message to show Code has begun 
   Serial.println("Starting Program .. \n");

   // Delay a few seconds 
   delay(2000);

   // Record time at which event loop began 
   startTime = millis();
}

void loop() {
  // put your main code here, to run repeatedly:

   // Record current time 
   currentTime = millis() - startTime;

   // Print continuity results when data is ready 
   if (results_ready == 1){

       // Convert from milliseconds to seconds
       t1_dec = t1/1000.0;
       t2_dec = t2/1000.0;

       // Calculate the burn time
       burnTime = t2_dec - t1_dec;
       
       // Print Results
       Serial.print("First Continuity Check: ");
       Serial.print(t1_dec);
       Serial.println("s");
       Serial.print("Second Continuity Check: ");
       Serial.print(t2_dec);
       Serial.println("s");
       Serial.print("Total Burn Time: ");
       Serial.print(burnTime);
       Serial.println("s");

       results_ready = 0;
    }

  Serial.println(" ");
  delay(500);
}

/********************* Interrupt Service Routines ***************************/

// record1: detect and record the first continuity loss
// inputs: none
// outputs: none
void record1(){
  
     // Store current time to later calculate burn rate
     t1 = currentTime;

     Serial.println("TEST 1");

     
     }

// record2: detect and record the second continuity loss
//          send message to print results to the console
// inputs:  none
// outputs: none
void record2(){
  
     // Store current time to calculate burn rate 
     t2 = currentTime;

      Serial.println("TEST 2");

     // Tell event loop to print results 
     results_ready = 1; 
  
  }
