/************************************************************* 
* myUART -- library for sending formated data over a UART    *
*           interface                                        *
*                                                            * 
* Author: Colton Acosta, cacost12@asu.edu                    *  
*                                                            * 
* Date: 1/7/2021                                             *
*                                                            * 
* Purpose: Convert data into byte arrays to be sent over a   *
*          UART interface and correctly reassembled to their *
*          original form                                     *
*                                                            * 
* Usage: Refer to the functions definitions below for usage. *
*        Each function transmits a particular data type in a *
*        standarized form over the interface. Use the python *
*        module to correctly interpret the data on the       *
*        receiving end                                       *
*************************************************************/ 
#include <avr/io.h>
#include <stdint.h>
#include <stdlib.h>
#include <util/delay.h>

#include "USART.h"

/* transmit_uint16t: Transmit a 16 bit integer 
   Input: 16 bit integer (uint16_t)
   Output: None, data is sent directly to the serial interface

   Function works by sending 3 bytes over the serial interface 
   If the first bit is a 1, This is the first byte
   The following bytes start with a 0 bit
*/
void transmit_uint16t(uint16_t input){

    /* Store the integer in two bytes */
    uint8_t numberBytes[] = {(uint8_t) ((0xff00 & input)>>  8), (uint8_t) (0x00ff & input)};

    /* Declare a byte array */
    uint8_t byteArray[] = {0,0,0};

    /* Make the first bit in the first byte 1 */
    byteArray[0] |= (1<<7);
   
    /* Move the most significant two bits to the first byte */
    byteArray[0] |= ((numberBytes[0] & (3<<6))>>6); 

    /* Bit shift the most significant byte 2 bits and set equal to 
       the second byte */
    byteArray[1] = ((numberBytes[0]<<1) & ~(1<<7));

    /* Move the most significant bit of the second byte to the least        significant bit of the tranmitted second byte */
    byteArray[1] |= ((numberBytes[1] & (1<<7))>>7); 

    /* Fill in the last transmitted byte */
    byteArray[2] |= (numberBytes[1] & ~(1<<7));

    /* Transmit the data */
    for(int i=0; i<3; ++i){
        transmitByte(byteArray[i]);
        _delay_ms(20);
    }

}
