/************************************************************* 
* myPorts -- custom library that converts data encoded into  *
*            a single byte into the corresponding register   *
*            values                                          *
*                                                            * 
* Author: Colton Acosta, cacost12@asu.edu                    * 
*                                                            * 
* Date: 1/1/2021                                             *
*                                                            * 
* Purpose: Library containing functions that parse byte data *
*          to be entered to the port registers for easy      *
*          reuse                                             * 
*                                                            * * Usage: copy library into working directory of project and  *
*        use the functions according to their descriptions   *
*        given below                                         *
*************************************************************/
#include <avr/io.h>

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

    /* Set the registers to the correct states */
    PORTB = blockB;
    PORTC = blockC;

}
