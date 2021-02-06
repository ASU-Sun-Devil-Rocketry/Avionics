This GUI program is capable of controlling the SDR Liquid Engine Switchbox to:
1) Automate Liquid Engine Startup
2) Provide Users an interactive environment to monitor data
3) Log sensor values into .txt file for post-test analysis


A couple things to keep in mind:

Any Arduino Board Boards required for com port auto detection
	Arduino UNO
	Arduino NANO / CH340


Current IMPORTS:
import tkinter as tk
import serial
import serial.tools.list_ports


Install the following modules: (type in command)
pip install pyserial