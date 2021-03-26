### Program for printing the contents of the serial monitor to the 
### console to emulate the arduino serial monitor 
import serial
import time

# readByte: Define function for reading a single byte and 
# converting it to a ordinal number
# input: serial port to read data from 
# output: byte read from the serial port
def readByte(serialPort):
   return(ord(serialPort.read(1)))

# Main loop 
def serialMonitor(serialPort):
   while(1):
      byte1 = readByte(serialPort)
      if (byte1>=128):
         byte2 = readByte(serialPort)
         byte3 = readByte(serialPort)
         byte1 -= 128
         byte1 *= (2**14)
         byte2 *= (2**7)
         print((byte1 + byte2 + byte3)/15625)
          
# Main code 
if __name__ == "__main__":

   PORT = '/dev/ttyUSB0'
   BAUDRATE = 9600
   TIMEOUT = 5

   serialPort = serial.Serial(PORT, BAUDRATE, TIMEOUT) 
   serialPort.flush()
   serialMonitor(serialPort)
