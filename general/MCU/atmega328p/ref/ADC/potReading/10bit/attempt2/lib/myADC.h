#ifndef MYADC_H
#define MYADC_H


#include <avr/io.h>
#include <stdint.h>


/* 10bitADC: function to reformat 10 bit ADC data into a 
             form that is easily interpreted by an     
             asyncrhonous data reciever 
   Inputs: Two bytes of data from the AVR ADC data registers,
           pointer to array containing memory for output bytes 
   Output: None, the function uses the input pointer to write             the reformated bytes directly to the stack 
   Usage: The UART interface must be configured ADLAR = 0, so
          that the ADCH register contains the most significant
          two bits and the ADCL register contains the rest of 
          the data. The function reformats the two bytes of 
          data such that the first bit of data indicates
          whether the byte currently being sent contains the 
          most or least significant bits. This is achieved by
          moving the most significant bit from the ADCL
          register to the least significant bit of the ADCH 
          data byte. The first bit of every byte indicates
          byte is being sent. 1 is most significant bytes and
          0 is least significant bytes */
void ADC_10bit(uint8_t ADCHbyte, uint8_t ADCLbyte, uint8_t *formatedData_ptr);





#endif
