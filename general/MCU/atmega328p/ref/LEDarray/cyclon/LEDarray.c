/************************************************************* * LEDarray -- program to make use of bit operations with an  *
*             array of 8 LEDs                                *
*                                                            * 
* Author: Colton Acosta, cacost12@asu.edu                    *
*                                                            * 
* Date: 1/1/2021                                             *
*                                                            * * Purpose: Light up a bunch of LEDs using bit operations     *
*                                                            * 
* Usage: Edit the Makefile to set avrdude microcontroller    *
*        specifications. Attach 8 LEDs to the D block of I/O *
*        pins on the microcontroller. Run the command make   *
*        flash to upload the code                            *
*************************************************************/ 
#include <avr/io.h>
#include<util/delay.h>

/* Define a constant time between LED flashes*/
#define DELAY_TIME 200

int main(void){

    /* Initialize all the D pins to output */
    DDRD |= 0xff; /* 11111111 */
    /* Initialize Counter variable */
    int i = 0;

    /* Enter Event Loop */
    while(1){
        
        /* Turn on LEDs in ascending order */
        while (i<7){
            PORTD = (1<<i);
            _delay_ms(DELAY_TIME);
            i++;
        }

        /* Turn on LEDs in descending order  */
        while(i>0){
            PORTD = (1<<i);
            _delay_ms(DELAY_TIME);
            i--;
        }

    }

    return(0);
}
