#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#include "binaryDebug.h"
#include "myUART.h"


int main(void){
   

    /* Create a 16 bit integer */
   // uint16_t number = 0b1100000001111111;
    
    /* Store the integer in two bytes */
    //uint8_t numberBytes[] = {(uint8_t) ((0xff00 & number) >>  8), (uint8_t) (0x00ff & number)};

    /* Declare a byte array */
    //uint8_t byteArray[] = {0,0,0};

    /* Make the first bit in the first byte 1 */
    //byteArray[0] |= (1<<7);
   
    /* Move the most significant two bits to the first byte */
    //byteArray[0] |= ((numberBytes[0] & (3<<6))>>6); 

    /* Bit shift the most significant byte 2 bits and set equal to 
       the second byte */
    //byteArray[1] = ((numberBytes[0]<<1) & ~(1<<7));

    /* Move the most significant bit of the second byte to the least        significant bit of the tranmitted second byte */
    //byteArray[1] |= ((numberBytes[1] & (1<<7))>>7); 

    /* Fill in the last transmitted byte */
    //byteArray[2] |= (numberBytes[1] & ~(1<<7));
/*
    printf("First Bit: ");
    printBinln((char) byteArray[0]);
    printf("Second Bit: ");
    printBinln((char) byteArray[1]);
    printf("Third Bit: ");
    printBinln((char) byteArray[2]);

*/
    transmit_uint16t(0b1100000001111111);
   
    return(0);
}
