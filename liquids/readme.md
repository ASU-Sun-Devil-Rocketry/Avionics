# SDR - Switchbox GUI
The following code on this repository has been designed to control the SDR Liquid Engine Switchbox to:
1) Automate Engine Startup
2) Display Engine State
3) Log Sensor Data

## GUI Layout
![GUI 3.0](https://github.com/nchennoju/SDR-Switch-Box/blob/master/SDR_GUI/img/v8.jpg)


A couple things to keep in mind:

**Arduino Boards required for com port auto detection

Current IMPORTS:
import tkinter as tk
import serial
import serial.tools.list_ports


Install the following modules: (type in command)
* pip install pyserial
* pip install python-tk
