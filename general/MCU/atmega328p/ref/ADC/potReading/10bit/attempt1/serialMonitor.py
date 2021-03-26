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
      serialPort.write(0xff)
      time.sleep(0.05)
      
      byte1 = readByte(serialPort)
      time.sleep(0.02)
      byte2 = readByte(serialPort)
      print(4*ord(byte1) + ord(byte2))        

# Main code 
if __name__ == "__main__":

   PORT = '/dev/ttyUSB1'
   BAUDRATE = 9600
   TIMEOUT = 5

   serialPort = serial.Serial(PORT, BAUDRATE, TIMEOUT) 
   serialPort.flush()
   serialMonitor(serialPort)
