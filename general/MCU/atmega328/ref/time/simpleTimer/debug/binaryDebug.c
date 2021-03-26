/************************************************************* * binaryDebug -- library for quick binary operations testing *
*                in order to test code, primarily meant for  *
*                bit toggling of microntrollers              *
*                                                            * * Author: Colton Acosta, cacost12@asu.edu                    *
*                                                            *
* Purpose: Print Binary expression to the console for        *
*          visualization of bit toggling procedures during   *
*          debuging                                          *
*                                                            * * Usage: Inlcude the header file in your debug code to       *
*        access the library functions                        *
*************************************************************/ 
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

/* printBin: print a character to the console in binary 
   Input: Unsigned Char value
   Output: None, function simply prints the binary code to the 
           console */
void printBin(char c){

    /* Loop over the bits in the car, shifting the byte each 
       loop and msking out the first bit */
    for(int i=0; i<8; ++i){
        printf("%d", !!((c<<i) & 0x80));
    }
}

/* printBinln: Same as printBin with newline character 
   Input: Unsigned Char value
   Output: None, function simply prints the binary code to the 
           console */
void printBinln(char c){

    /* Loop over the bits in the car, shifting the byte each 
       loop and msking out the first bit */
    for(int i=0; i<8; ++i){
        printf("%d", !!((c<<i) & 0x80));
    }

    printf("\n");
}


/* printBin16ln: print a 16bit int  character to the console in
                 binary 
   Input: uint16_t value
   Output: None, function simply prints the binary code to the 
           console */
void printBin16ln(uint16_t number){

    uint16_t power; 
    /* Loop over all bits and print to the screen */
    for (int i= 15; i>=0; --i){
        /* Create a bit mask for the digit */
        power = (1<<i);
       
        /* Print the digit */
        if (number & power){
            printf("%d", 1);
        } else{
            printf("%d", 0);
        }
         
    }
    /* Print a newline */
    printf("\n");    
}
