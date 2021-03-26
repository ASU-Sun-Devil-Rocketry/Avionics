/************************************************************* 
* myASCII -- convert a binary number to a configuration of   *
*            LED states                                      *
*                                                            * * Author: Colton Acosta, cacost12@asu.edu                    *
*                                                            *
* Date: 1/1/2021                                             *
*                                                            * 
* Purpose: Test the usage of the myPorts library with actual *
*          hardware                                          *
*                                                            * * Usage: Set up the myPorts library to use the pins that     *
*        are wired to the LEDs. Then run the make file. Hard *
*        code different LED state to test the code           (
*************************************************************/
#include <avr/io.h>
#include "lib/myPorts.h"

/* Set the State of the LEDs*/
uint8_t LEDstate = 0b10111000;

int main(void){

    /* Declare all the LEDs as outputs */
    DDRB |= 0b00111111; /* First 6 B pins are outputs */
    DDRC |= 0b00000011; /* First 2 C pins are outputs */

    /* Set the LEDs to the given state */
    multiBlockPort(LEDstate); 


    return(0);
}
