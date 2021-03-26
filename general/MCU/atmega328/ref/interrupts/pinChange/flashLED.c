/************************************************************* 
* flashLED -- a simple program to demonstrate the use of AVR *
*             interrupts                                     *
*                                                            * 
* Author: Colton Acosta, cacost12@asu.edu                    *  
*                                                            * 
* Date: 1/4/2021                                             *
*                                                            * 
* Purpose: Flash and LED on and off. Setup an interrupt to   *
*          turn on or off another LED when a button is       *
*          pressed                                           *
*                                                            * 
* Usage: Flash the code once and then press the button wired *
*        the AVRs INT0 interrupt pin                         *
*************************************************************/ 
#include <avr/io.h>
#include <stdint.h>
#include <util/delay.h>
#include <avr/interrupt.h>

#define DELAY_TIME 1000

/* Initialize Interrupt */
void initInterrupt(void){

    /* Enable Button Pin (PC2/PCINT10) as external interrupt */
    PCICR |= (1<<PCIE1);

    /* Configure interrupt to trigger when button changes state */
    PCMSK1 |= (1<<PCINT10);

    /* Set global interupt enable bit */
    sei();
}

/* Declare interrupt service routine */
ISR(PCINT1_vect){
    /* Toggle LED state if button was just pressed */
    if((((1<<PC2) & PINC) ^ (1<<PC2))){
        PORTC ^= (1<<1);
    }
}

int main(void){
    /* Initialization */
    DDRC |=( (1<<1) | 1); /* Set LED pins as output */
    PORTC |= (1<< PC2); /* Enable button pullup resistor */
    initInterrupt(); /* Setup button interrupt */
    PORTC &= (~(1<<1)); /* Make sure LED is initially off */

    /* Event Loop */
    while(1){
        /* Blink LED */
        PORTC ^= 1;
        _delay_ms(DELAY_TIME);
        
    }
    return(0);
}
