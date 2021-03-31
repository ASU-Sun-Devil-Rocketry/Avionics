/*******************************************************
* 25LC256 - library for interfacing with the 25LC256   *
*           EEPROM memory chip. Datasheet can be found *
*           in the doc directory                       *
*                                                      *
*                                                      *
* Author: Colton Acosta                                *
*                                                      *
* Purpose: Library containing functions needed to read *
*          and write data to the 25LC256 chip without  *
*          having to reference the datasheet           *
*                                                      *
* Usage: Copy library into lib directory of project    *
*        and use the functions according to their      *
*        descriptions given below                      *
*******************************************************/

#include <avr/io.h>
#include <util/delay.h>


