### Program for printing the contents of the serial monitor to the 
### console to emulate the arduino serial monitor 
import serial
import time

# readByte: Define function for reading a single byte and 
# converting it to a ordinal number
# input: serial port to read data from 
# output: byte read from the serial port
# Main code 
PORT = '/dev/ttyUSB1'
BAUDRATE = 9600
TIMEOUT = 5

def readByte(serialPort):
   return(ord(serialPort.read(1)))

serialPort = serial.Serial(PORT, BAUDRATE, TIMEOUT) 
serialPort.flush()

while(6):
   cmd = input("Enter a command: ")
   serialPort.write(cmd.encode())
   incomingByte = serialPort.read()
   print(incomingByte)
