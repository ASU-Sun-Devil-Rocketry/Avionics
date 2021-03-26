/************************************************************* 
* potRead -- Read the analog voltage across the wiper of a   *
*            potentiometer in order to test the              *
*            microcontroller analog to digital converter     *
*                                                            * 
* Author: Colton Acosta, cacost12@asu.edu                    *  
*                                                            * 
* Date: 1/3/2021                                             *
*                                                            * 
* Purpose: Provide a reference for using the analog to       *
*          digital converter for AVR microncontrollers       *
*                                                            * 
* Usage: Refer to the code to see the register usages        *
*************************************************************/ 
#include <avr/io.h>
#include <util/delay.h>
#include <stdint.h>
#include "lib/USART.h"

/* Define a delay time for event loop */
#define DELAY_TIME 1000 /* ms */

/* Function to initialize ADC */
static inline void initADC(void){

    /* Set the voltage reference to external voltage */
    ADMUX &= ~((1<<REFS1) | (1<<REFS0));

    /* Set the clock prescaler: ADC clock must be 50kHz to 200 Hz 
       For 16MHz clock speed, use value of 128 or 0b111 */
    ADCSRA |= ((1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0));

    /* Configure chip for 8 bit output */
    // ADMUX |= (1<<ADLAR);

    /* Enable the ADC */
    ADCSRA |= (1<<ADEN);

    /* Auto trigger enable */
    ADCSRA |= (1<<ADATE);

    /* Start First conversion */
    ADCSRA |= (1<<ADSC);
}

int main(void){

    /* Inits  */
    initUSART();
    initADC();

    /* Event Loop */
    while(1){
       
        /* Wait for start command from Python */ 
        while(~((1<<7) & UCSR0A)){
            transmitByte(UCSR0A);
            _delay_ms(20)
        } 
       
        while(1){ 
        /* Send two bytes*/
        transmitByte(ADCL);
        _delay_ms(20);
        transmitByte(ADCH);
        _delay_ms(20);}
    }

    return(0);
}
