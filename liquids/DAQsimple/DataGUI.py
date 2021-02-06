"""
Prototype GUI Interface for Data Aquisition
Displays Analog Voltage of Potentiometer position
Assumes Arduino Uno board is used
Written to be compatible with "DAQexperimental" Arduino script

Last Edit: June 7, 2020 
"""

__author__ = "Colton Acosta"
__credits__=["Nitish Chennoju"]


# GUI Imports
import tkinter as tk 
import Gauge
from PIL import Image,ImageTk
import numpy as np
from matplotlib import pyplot as plt

# Arduino Imports
from arduinoCom import *
from convertDAQ import *

# Setup GUI
root = tk.Tk()
root.geometry("600x600")
root.title("Analog Voltage Reading")
root.configure(background="black")

# Importing GUI images
SDRlogo = tk.PhotoImage(file='images/SDRLogo5.png')
SDRImage = Image.open("images/SDRlogont2.png")
SDRImage = SDRImage.resize((280,250),Image.ANTIALIAS)
SDR = ImageTk.PhotoImage(SDRImage)
SDRlabel = tk.Label(image=SDR,bg="black")
root.iconphoto(False,SDRlogo)
SDRlabel.pack()

# Display Status of Arduino Uno Connection
UnoPort = findArduinoUno(getPorts())
NanoPort = findArduinoNano(getPorts())
MegaPort = findArduinoMega(getPorts())

PortFrame =tk.Frame(root)
l1 = tk.Label(PortFrame,text="Connection Status: ",bg="black",fg="white",font="Helvetica 14")


if (UnoPort!="None"):
	l2 = tk.Label(PortFrame,text="Connected ["+UnoPort+"]",bg="black",fg="green",font="Helvetica 14")
	Port = UnoPort
	baudrate = 9600
elif (NanoPort!="None"):
	l2 = tk.Label(PortFrame,text="Connected ["+NanoPort+"]",bg="black",fg="green",font="Helvetica 14")	
	Port = NanoPort
	baudrate = 115200
elif (MegaPort!="None"):
	l2 = tk.Label(PortFrame,text="Connected ["+MegaPort+"]",bg="black",fg="green",font="Helvetica 14")
	Port = MegaPort
	baudrate = 9600
else:
	l2 = tk.Label(PortFrame,text="Disconnected", bg="black",fg="red",font="Helvetica 14")
	Port = "None"
	baudrate = 9600

l1.pack(side="left")
l2.pack(side="left")
PortFrame.pack(pady=20)

# Insert Gauge
VoltageGage = Gauge.Gauge(root,"black",5)
VoltageGage.setText("Start","Voltage")
VoltageGage.getWidget().pack(pady=30)

# Connect to Arduino Serial Port
if (Port!="None"):
   serialData = serial.Serial(Port[0:4],baudrate=baudrate,timeout=1)

# Initialize Data Vector for Recording
dataStorage = []


# Start Live GUI

try: 
	while True:

		if(Port!="None"):

		   # Read Data point
		   data = getData(serialData)

		   # Convert Data to manageable form
		   dataf = serialFilter(data)

		   if (dataf!="Null"):

			   # Convert to voltage
			   voltage = voltage05(data)

			   # Calculate angle (-30V-210 deg, 5V-0 deg)
			   angle = voltage*42 -30

			   # Round Voltage
			   voltformat = "{:.3f}".format(voltage)

			   # Record Data
			   dataStorage.append(voltage)

			   # Reconfigure Gauge
			   VoltageGage.setAngle(voltage)
			   VoltageGage.setText(voltformat,"Voltage (V)")

			   # Update
			   root.update()

		root.update()
except:
	# Record Data to txt file
	myData = open("voltageData.txt","w+")

	for i in range(len(dataStorage)):
		myData.write(str(dataStorage[i])+"\n")

	myData.close()

	# Plot Recorded Data
	plt.plot(range(len(dataStorage)),dataStorage)
	plt.xlabel('Sample')
	plt.ylabel('Voltage (V)')
	plt.title('Sample Signal')
	plt.show()



