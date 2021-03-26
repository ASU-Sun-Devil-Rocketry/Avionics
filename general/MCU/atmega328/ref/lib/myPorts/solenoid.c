/*************************************************************
* solenoid -- test code for solenoid status communications   *
*             functions                                      *
*                                                            * 
* Author: Colton Acosta, cacost12@asu.edu                    *  
*                                                            * 
* Date: 12/27/2020                                           * 
*                                                            * 
* Purpose: Library file for testing solenoid communications  *
*          functions                                         *
*                                                            * 
* Usage: Meant for testing only. Use the main serial library *
*        for finished code                                   *
*************************************************************/ 
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/* Bool values for ON and OFF of solenoids */
bool ON = true;
bool OFF = false;

/* printBin: print a character to the console in binary 
   Input: Unsigned Char value
   Output: None, function simply prints the binary code to the 
           console */
void printBin(char c){

    /* Loop over the bits in the car, shifting the byte each 
       loop and msking out the first bit */
    for(int i=0; i<8; ++i){
        printf("%d", !!((c<<i) & 0x80));
    }
}

/* printBinln: Same as printBin with newline character 
   Input: Unsigned Char value
   Output: None, function simply prints the binary code to the 
           console */
void printBinln(char c){

    /* Loop over the bits in the car, shifting the byte each 
       loop and msking out the first bit */
    for(int i=0; i<8; ++i){
        printf("%d", !!((c<<i) & 0x80));
    }

    printf("\n");
}

/* solenoidAct: Set Solenoid State to ON or OFF 
   Inputs: Current Solenoid State, Number of solenoid 
           to actuate (1-8), ON or OFF command
   Output: Byte with new status of solenoids
*/
char solenoidAct(char currentState ,int solNum, bool onOff){

    /* Check that solenoid to actuate is a valid solenoid */
    while (solNum<1 || solNum>8){
        printf("Invalid Solenoid Number. Enter a valid number (1-8): ");
        scanf("%d", &solNum);
    }

    /* Determine if Solenoid is to be turned off or on */
    if(onOff){

        /* Create a byte to represent the solenoid to 
           be actuated in the ON state */
        int actuateSol = (1<<(solNum-1));

        /* Update current state byte */
        currentState |= actuateSol;

        return (currentState);
    }else{
        /* Create a bit string with a 0 in solenoid position */
        int actuateSol = (1<<(solNum-1));
        actuateSol = ~actuateSol;
      
        /* Use a bitwise AND to turn off solenoid */
        currentState = currentState & actuateSol;

        return(currentState);
        
    }
}

int main(){

    /* Instantiate Solenoid State */
    printf("Enter a solenoid intial state: ");
    int input;
    scanf("%x", &input);
    char solenoidState = input;
    printf("Initial Solenoid State: ");
    printBinln(solenoidState);

    /* Ask the user which solenoid to actuate */
    printf("Enter a solenoid to actuate (1 to 8): ");
    int solenoid;
    scanf("%d", &solenoid);

    /* Ask if they want to turn it on or off */
    char answer;
    printf("Do you want to turn the solenoid on or off? (H or L): ");
    scanf(" %c", &answer);
    
    /* Check to make sure they entered a valid answer */
    while(answer!='H' && answer!='L'){
        printf("Invalid response. Try again (H or L): ");
        scanf("%c", &answer);
    }

    /* Actuate Solenoid */
    if(answer=='H'){
        solenoidState = solenoidAct(solenoidState, solenoid, ON);
    }else{
        solenoidState = solenoidAct(solenoidState, solenoid, OFF);
    }

    /* Print state of Solenoid to console */
    printf("State of Solenoids: ");
    printBin(solenoidState);
    printf("\n");

    return(0);
}
