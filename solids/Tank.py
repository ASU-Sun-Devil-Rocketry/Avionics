# !/usr/bin/env python3
from tkinter import *

#UNCOMMENT IF TESTING
#import time
#import tkinter as tk

class Tank:

    def __init__(self, root, background, title, fluidColor, width, height):
        padding = 15

        self.c = Canvas(root, width=width, height=height, bg=background, highlightthickness=0)
        self.width = width
        self.height = height

        self.top = None
        self.right = None
        self.bottom = None
        self.left = None

        self.rect = self.c.create_rectangle(width/4.0, 0, width*(3/4.0), height-1, outline='white')
        self.fill = self.c.create_rectangle((width/4.0) + 1, 50,width*(3/4.0)-1, height-2, fill=fluidColor)

        self.pressure = self.c.create_text(width / 2.0, (height / 2.0) - 1.25*padding, font=("Arial", 11, 'bold'), fill="white", text=title)
        self.pressure = self.c.create_text(width/2.0, (height/2.0), font=("Arial", 8), fill="white", text='psi')
        self.percentage = self.c.create_text(width/2.0, (height/2.0) + padding, font=("Arial", 8), fill="white", text='%')
        self.temperature = self.c.create_text(width/2.0, (height/2.0) + 2*padding, font=("Arial", 8), fill="white", text='tmp')


    def setTankLevel(self, percent):
        self.c.coords(self.fill, (self.width/4.0) + 1, self.height - ((percent/100.0)*self.height-2) - 2, self.width*(3/4.0)-1, self.height-2)
        self.c.itemconfig(self.percentage, text=str(percent) + " %")

    def setTankReadout(self, tmp, pressure):
        self.c.itemconfig(self.pressure, text=str(pressure) + ' psi')
        self.c.itemconfig(self.temperature, text=str(tmp) + ' °C')

    def setNeighbors(self, top, right, bottom, left):
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left

    def getWidget(self):
        return self.c

'''#TEST CODE
win = tk.Tk()
win.title("ELEMENT TEST")
win.geometry("800x500")
win.configure(bg='black')

t = Tank(win, 'black', 'BOOM', '#1d2396', 500, 300)
t.getWidget().pack(side='bottom')

while True:
    for i in range(101):
        t.setTankLevel(i)
        t.setTankReadout(i, i)
        time.sleep(0.01)
        win.update()
    for i in range(101):
        t.setTankLevel(100 - i)
        t.setTankReadout(i, i)
        time.sleep(0.01)
        win.update()

win.mainloop()'''