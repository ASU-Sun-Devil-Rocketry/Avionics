#ifndef MYUART_H
#define MYUART_H


//#include <avr/io.h>
#include <stdint.h>
#include <stdlib.h>

//#include "USART.h"

/* transmit_uint16t: Transmit a 16 bit integer 
   Input: 16 bit integer (uint16_t)
   Output: None, data is sent directly to the serial interface

   Function works by sending 3 bytes over the serial interface 
   If the first bit is a 1, This is the first byte
   The following bytes start with a 0 bit
*/
void transmit_uint16t(uint16_t input);




#endif
