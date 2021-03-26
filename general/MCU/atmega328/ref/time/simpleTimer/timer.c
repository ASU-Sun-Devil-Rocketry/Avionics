/************************************************************* 
* simpleTimer -- send the current time from the AVR time     *
*                registers to the UART interface and display *
*                on a serial monitor                         *
*                                                            * 
* Author: Colton Acosta, cacost12@asu.edu                    *  
*                                                            * 
* Date: 1/7/2021                                             *
*                                                            * 
* Purpose: Demonstrate how to use the AVRs internal timing   *
*          hardware by printing the time to the serial       *
*          monitor                                           *
*                                                            * 
* Usage: Program is meant to be run on a microcontroller     *
*        a crytstal set at 16 MHz. Program uses the simple 8 *
*        bit timer to count up in terms of tens of ms        *
*************************************************************/ 
#include <avr/io.h>
#include <stdint.h>
#include <avr/interrupt.h>
#include <util/delay.h>

#include "lib/USART.h"
#include "lib/myUART.h"

/* Initialize Timer Hardware */
static inline void initTimer(void){

    /* Normal Mode, with speed 16MHz/1024 = 15625 Hz */
    TCCR1B |= ((1<<CS12) | (1<<CS10));

}

int main(void){

    /* Inits */
    initUSART();
    initTimer();
    TCNT1 = 0;

    /* Event Loop */
    while(1){
       
    /* Transmit current time to serial port */
    transmit_uint16t(TCNT1); 

    }


    return(0);
}
