# !/usr/bin/env python3
from tkinter import *

#UNCOMMENT IF TESTING
'''import time
import tkinter as tk'''

class Nozzle:

    def __init__(self, root, background, width, height):
        padding = 25

        self.top = None
        self.right = None
        self.bottom = None
        self.left = None

        self.c = Canvas(root, width=width, height=height, bg=background, highlightthickness=0)
        self.width = width
        self.height = height

        self.plot = []
        self.plot.append((1, 1))
        self.plot.append((width - 1, 1))
        self.plot.append((width - 1, height * 0.1))
        self.plot.append((0.9 * width, height * 0.1))
        self.plot.append((0.9 * width, height * 0.7))
        self.plot.append((0.6 * width, height * 0.9))
        self.plot.append((0.7*width, height-1))
        self.plot.append((0.3*width, height-1))
        self.plot.append((0.4 * width, height * 0.9))
        self.plot.append((0.1 * width, height * 0.7))
        self.plot.append((0.1 * width, height * 0.1))
        self.plot.append((1, height * 0.1))

        self.base = self.c.create_polygon(self.plot, outline='white')

        self.thrust = self.c.create_text(width/2.0, (height/2.0) - padding, font=("Arial", 10), fill="white", text='thrust')
        self.pressure = self.c.create_text(width/2.0, height/2.0, font=("Arial", 10), fill="white", text='pressure')


    def setNeighbors(self, top, right, bottom, left):
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left

    def getWidget(self):
        return self.c

    def setNozzleReadout(self, thrust, pressure):
        self.c.itemconfig(self.thrust, text='LC: ' + str(thrust) + ' N')
        self.c.itemconfig(self.pressure, text='PT: ' + str(pressure) + ' psi')

#TEST CODE
'''win = tk.Tk()
win.title("ELEMENT TEST")
win.geometry("800x500")
win.configure(bg='black')

n = Nozzle(win, 'black', 200, 400)
n.getWidget().pack(side='bottom')

while True:
    for i in range(100):
        n.setNozzleReadout(i, i)
        time.sleep(0.01)
        win.update()

win.mainloop()'''