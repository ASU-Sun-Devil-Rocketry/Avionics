import tkinter as tk
import serial
import serial.tools.list_ports
from serial import SerialException
import threading

import Gauge
import RelaySwitch
import PandID

class Controls:
    def __init__(self, plumbing):
        self.plumbing = plumbing
        root = tk.Tk()
        root.title("SDR - Liquid Engine Dashboard");
        root.configure(background="black")

        tk.Label(root, text="SDR - Liquid Engine Dashboard", bg="black", fg="white", font="Arial 30").pack(pady=40)

        # ARDUINO STATUS
        status = self.findArduino(self.getPorts())
        connectionLabel = tk.Label(root, text='CONNECTED' + status, bg="black", fg="#41d94d", font="Arial 14")
        if (status == "None"):
            arduinoSwitchbox = serial.Serial()
            connectionLabel.configure(text='DISCONNECTED' + status, fg="#ed3b3b")
        else:
            arduinoSwitchbox = serial.Serial(status.split()[0], 9600)
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
        s = tk.Button(root, text="STARTUP", padx=40, pady=10, font="Verdana 14", bg="yellow",
                      command=threading.Thread(target=self.startup).start, activebackground="yellow")
        off = tk.Button(root, text="All OFF", padx=30, pady=10, font="Verdana 14", bg="RED", command=allOff,
                        activebackground="RED")

        s.pack(pady=pad)
        off.pack(pady=pad)

        # ------------------------ DATA LOGGER GUI GAUGE -----------------------------
        g1 = Gauge.Gauge(g, 'black')
        g1.setText("Nan", "A0")
        g1.getWidget().pack(side="left")
        g2 = Gauge.Gauge(g, 'black')
        g2.setText("Nan", "A1")
        g2.getWidget().pack(side="left")
        g3 = Gauge.Gauge(h, 'black')
        g3.setText("Nan", "A2")
        g3.getWidget().pack(side="left")
        g4 = Gauge.Gauge(h, 'black')
        g4.setText("Nan", "A3")
        g4.getWidget().pack(side="right")
        g.pack()
        h.pack()

        print(status)
        prevCon = True

    # Returns list of all accessible serial ports
    def getPorts(self):
        portData = serial.tools.list_ports.comports()
        return portData

        # Returns COM port of Arduino if detected by computer. User for switchbox

    def findArduino(self, portsFound):
        numConnections = len(portsFound)
        for i in range(0, numConnections):
            if ('Uno' in str(portsFound[i]) or 'Nano' in str(portsFound[i]) or 'CH340' in str(portsFound[i])):
                return str(portsFound[i])
        return "None"

    def conv(self, str):
        return str[2:len(str) - 5]

    def startup(self):
        print("Startup")
        switch1.setLedState(True)
        plumbing.one.setState(True)
        root.update()
        plumbing.getWindow().update()
        time.sleep(1)
        switch1.setLedState(False)
        plumbing.one.setState(False)
        switch2.setLedState(True)
        plumbing.two.setState(True)
        root.update()
        plumbing.getWindow().update()
        time.sleep(1)
        switch2.setLedState(False)
        plumbing.two.setState(False)
        switch3.setLedState(True)
        plumbing.three.setState(True)
        root.update()
        plumbing.getWindow().update()
        time.sleep(1)
        switch3.setLedState(False)
        plumbing.three.setState(False)
        root.update()
        plumbing.getWindow().update()
        time.sleep(1)

    def allOff(self):
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