# !/usr/bin python3
"""
SDR_LiquidGUI.py: A python GUI developed to interface with SDR rocketry's liquid engine switchbox.
    The interface consists of elements which write and read data to and from the Arduino to provide a
    fully interactive program GUI. The program is meant to run on the launch computer which is hardwired
    to the switchbox arduino via USB. Once the program is running, users are encouraged to move the
    window to fit their needs.
    On one window, switch box relay controls will be present along with a series of Gauge objects
    which display sensor readings. Additionally, all realtime sensor readings are logged onto a .txt
    file onto the computer running the python script.
    On the other window, an interactive P&ID vitual diagram is present with sensor readings updating
    graphical elements. The P&ID enables an easy method to view the status of the engine at any time.
"""

__author__ = "Nitish Chennoju"
__credits__ = ["Colton Acosta"]

import time
import serial
import serial.tools.list_ports
from serial import SerialException
import tkinter as tk

# Custom Classes
import Gauge
import RelaySwitch
import PandID


# Returns list of all accessible serial ports
def getPorts():
    portData = serial.tools.list_ports.comports()
    return portData

    # Returns COM port of Arduino if detected by computer. User for switchbox


def findArduino(portsFound):
    numConnections = len(portsFound)
    for i in range(0, numConnections):
        if ('Uno' in str(portsFound[i]) or 'Nano' in str(portsFound[i]) or 'CH340' in str(portsFound[i])):
            return str(portsFound[i])
    return "None"


def conv(str):
    return str[2:len(str) - 5]


def main():
    def startup():
        print("Startup")

    def allOff():
        arduinoSwitchbox.write(b'8')
        switch1.setLedState(False)
        switch2.setLedState(False)
        switch3.setLedState(False)
        switch4.setLedState(False)
        switch5.setLedState(False)
        switch6.setLedState(False)
        plumbing.one.setState(False)
        plumbing.two.setState(False)
        plumbing.three.setState(False)
        plumbing.four.setState(False)
        plumbing.five.setState(False)
        plumbing.six.setState(False)
        print("All OFF COMPLETE")

    # Spacing constants within GUI
    pad = 10
    gridLen = 85

    # Get file name from user
    print("Enter file name (don't include file extension): ", end='')
    fileName = input() + ".txt"

    # Initialize GUI Windows
    plumbing = PandID.Engine_Plumbing(gridLen)  # P&ID diagram window

    root = tk.Tk()
    root.title("SDR - Liquid Engine Dashboard");
    root.configure(background="black")

    tk.Label(root, text="SDR - Liquid Engine Dashboard", bg="black", fg="white", font="Arial 30").pack(pady=40)

    # ARDUINO STATUS
    status = findArduino(getPorts())
    connectionLabel = tk.Label(root, text='CONNECTED' + status, bg="black", fg="#41d94d", font="Arial 14")
    if (status == "None"):
        arduinoSwitchbox = serial.Serial()
        connectionLabel.configure(text='DISCONNECTED' + status, fg="#ed3b3b")
    else:
        arduinoSwitchbox = serial.Serial(status.split()[0], 115200)
    connectionLabel.pack()

    # RELAY Switches created
    a = tk.Frame(root, bg='black')
    b = tk.Frame(root, bg='black')
    c = tk.Frame(root, bg='black')
    d = tk.Frame(root, bg='black')
    switch1 = RelaySwitch.Buttons(a, 0, arduinoSwitchbox, "Relay 1", plumbing.one)
    switch2 = RelaySwitch.Buttons(b, 1, arduinoSwitchbox, "Relay 2", plumbing.two)
    switch3 = RelaySwitch.Buttons(c, 2, arduinoSwitchbox, "Relay 3", plumbing.three)
    switch4 = RelaySwitch.Buttons(d, 3, arduinoSwitchbox, "Relay 4", plumbing.four)
    switch5 = RelaySwitch.Buttons(a, 0, arduinoSwitchbox, "Relay 5", plumbing.five)
    switch6 = RelaySwitch.Buttons(b, 1, arduinoSwitchbox, "Relay 6", plumbing.six)
    switch7 = RelaySwitch.StepperSlider(c, arduinoSwitchbox)
    switch8 = RelaySwitch.StepperSlider(d, arduinoSwitchbox)

    a.pack()
    b.pack()
    c.pack()
    d.pack()

    g = tk.Frame(root)
    h = tk.Frame(root)
    s = tk.Button(root, text="STARTUP", padx=40, pady=10, font="Verdana 14", bg="yellow", command=startup,
                  activebackground="yellow")
    off = tk.Button(root, text="All OFF", padx=30, pady=10, font="Verdana 14", bg="RED", command=allOff,
                    activebackground="RED")

    s.pack(pady=pad)
    off.pack(pady=pad)

    # ------------------------ DATA LOGGER GUI GAUGE -----------------------------
    g1 = Gauge.Gauge(g, 'black', 5)
    g1.setText("Nan", "A0")
    g1.getWidget().pack(side="left")
    g2 = Gauge.Gauge(g, 'black', 5)
    g2.setText("Nan", "A1")
    g2.getWidget().pack(side="left")
    g3 = Gauge.Gauge(h, 'black', 5)
    g3.setText("Nan", "A2")
    g3.getWidget().pack(side="left")
    g4 = Gauge.Gauge(h, 'black', 5)
    g4.setText("Nan", "A3")
    g4.getWidget().pack(side="right")
    g.pack()
    h.pack()

    prevCon = True

    # Main Program Loop

    while True:
        # ARDUINO CONNECTION CHECK
        status = findArduino(getPorts())
        if (status == "None"):
            connectionLabel.configure(text='DISCONNECTED ' + status, fg="#ed3b3b")
            g1.setText("Nan", "A0")
            g2.setText("Nan", "A1")
            g3.setText("Nan", "A2")
            g4.setText("Nan", "A3")
            prevCon = False
        elif (not prevCon and status != 'None'):
            try:
                arduinoSwitchbox = serial.Serial(status.split()[0], 115200)
                time.sleep(5)
                connectionLabel.configure(text='CONNECTED ' + status, fg="#41d94d")
                switch1.setArduino(arduinoSwitchbox)
                switch2.setArduino(arduinoSwitchbox)
                switch3.setArduino(arduinoSwitchbox)
                switch4.setArduino(arduinoSwitchbox)
                switch5.setArduino(arduinoSwitchbox)
                switch6.setArduino(arduinoSwitchbox)
                switch7.setArduino(arduinoSwitchbox)
                switch8.setArduino(arduinoSwitchbox)
                prevCon = True
            except SerialException:
                print("ERROR: LOADING...")
        else:
            connectionLabel.configure(text='CONNECTED ' + status, fg="#41d94d")

        # Attempting to get data from Arduino
        try:
            strSerial = conv(str(arduinoSwitchbox.readline()))
        except SerialException:
            strSerial = ''
            print("ERROR")

        data = strSerial.split("\\t")

        plumbing.s2.setPercentage(switch7.getVal())
        plumbing.s1.setPercentage(switch8.getVal())


        if (plumbing.one.getState()):
            plumbing.p5.setState(True)
            plumbing.ps1.setPipes(True)
            plumbing.p8.setState(True)
            plumbing.o1.setPipes(True)
            plumbing.p14.setState(True)
            plumbing.p16.setState(True)
            plumbing.s2.setPipes(False, False, False, True)
        else:
            plumbing.p5.setState(False)
            plumbing.ps1.setPipes(False)
            plumbing.p8.setState(False)
            plumbing.o1.setPipes(False)
            plumbing.p14.setState(False)
            plumbing.p16.setState(False)
            plumbing.s2.setPipes(False, False, False, False)

        if (plumbing.three.getState()):
            plumbing.p7.setState(True)
            plumbing.ps3.setPipes(True)
            plumbing.p10.setState(True)
            plumbing.p13.setState(True)
            plumbing.s1.setPipes(True, False, False, False)
        else:
            plumbing.p7.setState(False)
            plumbing.ps3.setPipes(False)
            plumbing.p10.setState(False)
            plumbing.p13.setState(False)
            plumbing.s1.setPipes(False, False, False, False)

        # PROBLEMS
        if (plumbing.five.getState()):
            plumbing.s2.setPipes(False, True, True, False)
            plumbing.p19.setState(True)
            plumbing.p20.setState(True)
        else:
            plumbing.p19.setState(False)
            plumbing.p20.setState(False)

        if (plumbing.six.getState()):
            plumbing.o2.setPipes(True)
            plumbing.p17.setState(True)
            plumbing.p18.setState(True)
            plumbing.p22.setState(True)
            plumbing.ps2.setPipes(True)
            plumbing.tp1.setPipes(True)
            plumbing.p21.setState(True)
            plumbing.p20.setState(True)
        else:
            plumbing.o2.setPipes(False)
            plumbing.p17.setState(False)
            plumbing.p18.setState(False)
            plumbing.p22.setState(False)
            plumbing.ps2.setPipes(False)
            plumbing.tp1.setPipes(False)
            plumbing.p20.setState(False)

        if (plumbing.s2.getPercentage() > 0 and plumbing.s2.left.getState()):
            plumbing.s2.setPipes(False, False, True, True)
            plumbing.p19.setState(True)
            plumbing.p20.setState(True)
        if (plumbing.s1.getPercentage() > 0 and plumbing.s1.top.getState()):
            plumbing.s1.setPipes(True, False, False, True)
            plumbing.o2.setPipes(True)
            plumbing.p17.setState(True)
            plumbing.p18.setState(True)
            plumbing.p22.setState(True)
            plumbing.ps2.setPipes(True)
            plumbing.tp1.setPipes(True)
            plumbing.p21.setState(True)
            plumbing.p20.setState(True)

        if (data[0] == "Time"):
            file = open(fileName, "a")
            file.write(strSerial[0:len(strSerial) - 2] + "\n")
            print(strSerial[0:len(strSerial) - 2])
            file.close()

            # P&ID INITIAL STATE
            plumbing.p1.setState(True)
            plumbing.p2.setState(True)
            plumbing.p3.setState(True)
            plumbing.p4.setState(True)
            plumbing.p6.setState(True)
            plumbing.p9.setState(True)
            plumbing.p11.setState(True)
            plumbing.p12.setState(True)
            plumbing.p15.setState(True)
            plumbing.one.setPipes(False, True, False, False)
            plumbing.three.setPipes(False, False, False, True)
            plumbing.five.setPipes(True, False, False, False)
            plumbing.six.setPipes(False, False, False, True)


        elif (len(data) > 4 and data[0] != "Time"):
            file = open(fileName, "a")
            file.write(strSerial[0:len(strSerial) - 2] + "\n")
            print('\t'.join(data))
            file.close()
            g1.setAngle(abs(5 * float(data[1])) / 1023.0)
            g1.setText(data[1], "A0")
            g2.setAngle(abs(5 * float(data[2])) / 1023.0)
            g2.setText(data[2], "A1")
            g3.setAngle(abs(5 * float(data[3])) / 1023.0)
            g3.setText(data[3], "A2")
            g4.setAngle(abs(5 * float(data[4])) / 1023.0)
            g4.setText(data[4].replace('\n', ''), "A3")

        root.update()
        plumbing.getWindow().update()
        #plumbing.updatePipeStatus()


if __name__ == "__main__":
    main()