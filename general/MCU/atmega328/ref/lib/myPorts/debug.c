#include <stdio.h>
#include<stdlib.h>
typedef u_int8_t uint8_t;

void printBin(uint8_t c){

    /* Loop over the bits in the car, shifting the byte each 
       loop and msking out the first bit */
    for(int i=0; i<8; ++i){
        printf("%d", !!((c<<i) & 0x80));
    }
}
/* multiBlockPort: takes one byte of digital Output data and 
                   parses it cross specified ports 
   Input: One byte of data
   Output: none, the program simply writes the data contained 
           within the input byte to the specified registers */
void multiBlockPort(uint8_t byte){

    /* Map Ports: manually change 
       Bits 0-5 are for port B (0-5) 
       Bits 6-7 are for port C (0-1) */

    /* Split the byte into two bytes for each pin block */
    uint8_t blockB = 0b00111111;
    uint8_t blockC = ~(blockB);
    blockB &= byte;
    blockC &= byte; 

    /* Shift the two bytes so that the pins match up */
    blockC = (blockC >> 6);

    /* Print the results */
    printf("Results of Block B: ");
    printBin(blockB);
    printf("\n");
    printf("Results of Block C: ");
    printBin(blockC);
    printf("\n");
}


int main(){

    /* Get Binary Number from the user */
    printf("Enter a hex number: ");
    int ans;
    scanf("%x", &ans);
    uint8_t newAns = (uint8_t) ans;

    /* Print the Binary Representation */
    printf("The Number is: ");
    printBin(newAns);
    printf("\n");

    /* Run the function */
    multiBlockPort(ans);

   return(0);
}
