/************************************************************* 
* buttonUART -- program to send the status of a button push  *
*               over the UART interface                      *
*                                                            * 
* Author: Colton Acosta, cacost12@asu.edu                    *  
*                                                            * 
* Date: 1/5/2021                                             *
*                                                            * 
* Purpose: Send the status of a button press to the serial   *
*          port                                              *
*                                                            * 
* Usage: Press the button and monitor the input to the       *
*        serial port                                         *
*************************************************************/ 
#include <avr/io.h>
#include <stdint.h>
#include <util/delay.h>
#include "lib/USART.h"

int main(void){

    /* Enable the button pullup resister */
    PORTC |= (1<<PC2);
   
    /* Initialize serial comms */
    initUSART();

    /* Event Loop */
    while(1){
        
        transmitByte(PINC);
        _delay_ms(50);
    }



    return(0);
}

