/************************************************************* 
* simpleUART -- convert numbers entered to serial interface  *
*            into  LED states                                *
*                                                            *
* Author: Colton Acosta, cacost12@asu.edu                    *
*                                                            *
* Date: 1/1/2021                                             *
*                                                            * 
* Purpose: Test the UART serial interface of the atmega328p  *
*                                                            *
* Usage: Set up the myPorts library to use the pins that     *
*        are wired to the LEDs. Then run the make file. Hard *
*        code different LED state to test the code           *
*************************************************************/
#include <avr/io.h>
#include <util/delay.h>
#include <stdint.h>
#include <inttypes.h>
#include "lib/pinDefines.h"
#include "lib/USART.h"

#include "lib/myPorts.h"

int main(void){
    
    char serialCharacter;
   
    /* Declare all the LEDs as outputs */
    DDRB |= 0b00111111; /* First 6 B pins are outputs */
    DDRC |= 0b00000011; /* First 2 C pins are outputs */

    /* Initialize the UART interface */
    initUSART();
    printString("Hello World!\r\n");

    /* Event Loop */
    while(1){
        serialCharacter = receiveByte();
        transmitByte(serialCharacter);
        multiBlockPort((uint8_t) serialCharacter);        
    }

    return(0);
}
