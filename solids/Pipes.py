# !/usr/bin/env python3
from tkinter import *

#UNCOMMENT IF TESTING
#import time
#import tkinter as tk

"""
The following class makes it simple to connect different GUI P&ID objects together with pipes.
The PIPE Class operates on five main parameters: line1, line2, line3, line4, fill

All 5 parameters are of the data type boolean and control the type of pipe and whether fluid is running through it
(repsectively)

The booleans line# correspond to which side gets a pipe:
line1: 12:00
line2: 3:00
line3: 6:00
line4: 9:00

        ln1
        
  ln4    P    ln2
   
        ln3
        
By modulating these input parameters, any pipe can be designed to fit the GUI P&ID.
"""

class Pipe:

    def __init__(self, root, background, width, height, line_1, line_2, line_3, line_4, fluidColor, fill):
        self.c = Canvas(root, width=width, height=height, bg=background, highlightthickness=0)
        self.width = width
        self.height = height

        self.line1 = line_1
        self.line2 = line_2
        self.line3 = line_3
        self.line4 = line_4

        self.top = None
        self.right = None
        self.bottom = None
        self.left = None

        self.state = False
        self.fluidColor = fluidColor

        # DRAW PIPES
        if(fill):
            self.f0 = self.c.create_rectangle(7 * width / 16.0, 7 * height / 16.0, 9 * width / 16.0, 9 * height / 16.0,
                                              fill=fluidColor)
        else:
            self.f0 = self.c.create_rectangle(7 * width / 16.0, 7 * height / 16.0, 9 * width / 16.0, 9 * height / 16.0,
                                              fill='black')

        if (line_1):
            xy = [(7 * width / 16.0, 0), (7 * width / 16.0, 7 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(9 * width / 16.0, 0), (9 * width / 16.0, 7 * height / 16.0)]
            self.c.create_line(xy2, width=1, fill='white')
            if(fill):
                self.f1 = self.c.create_rectangle((7 * width / 16.0) + 1, 0, (9 * width / 16.0) - 1, (7 * height / 16.0) + 1,
                                                  fill=fluidColor, outline="")
            else:
                self.f1 = self.c.create_rectangle((7 * width / 16.0) + 1, 0, (9 * width / 16.0) - 1,
                                                  (7 * height / 16.0) + 1,
                                                  fill='black', outline = "")
        else:
            xy = [(7 * width / 16.0, 7 * height / 16.0), (9 * width / 16.0, 7 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')
        if (line_2):
            xy = [(9 * width / 16.0, 7 * height / 16.0), (width, 7 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(9 * width / 16.0, 9 * height / 16.0), (width, 9 * height / 16.0)]
            self.c.create_line(xy2, width=1, fill='white')
            if(fill):
                self.f2 = self.c.create_rectangle(9 * width / 16.0, (7 * height / 16.0) + 1, width,
                                                  (9 * height / 16.0) - 1,
                                                  fill=fluidColor, outline="")
            else:
                self.f2 = self.c.create_rectangle(9 * width / 16.0, (7 * height / 16.0) + 1, width,
                                                  (9 * height / 16.0) - 1,
                                                  fill='black', outline="")
        else:
            xy = [(9 * width / 16.0, 7 * height / 16.0), (9 * width / 16.0, 9 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')
        if (line_3):
            xy = [(7 * width / 16.0, 9 * height / 16.0), (7 * width / 16.0, height)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(9 * width / 16.0, 9 * height / 16.0), (9 * width / 16.0, height)]
            self.c.create_line(xy2, width=1, fill='white')
            if(fill):
                self.f3 = self.c.create_rectangle((7 * width / 16.0) + 1, 9 * height / 16.0, (9 * width / 16.0) - 1,
                                                  height,
                                                  fill=fluidColor, outline="")
            else:
                self.f3 = self.c.create_rectangle((7 * width / 16.0) + 1, 9 * height / 16.0, (9 * width / 16.0) - 1,
                                                  height,
                                                  fill='black', outline="")
        else:
            xy = [(7 * width / 16.0, 9 * height / 16.0), (9 * width / 16.0, 9 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')
        if (line_4):
            xy = [(0, 7 * height / 16.0), (7 * width / 16.0, 7 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(0, 9 * height / 16.0), (7 * width / 16.0, 9 * height / 16.0)]
            self.c.create_line(xy2, width=1, fill='white')
            if(fill):
                self.f4 = self.c.create_rectangle(0, (7 * height / 16.0) + 1, (7 * width / 16.0) + 1,
                                                  (9 * height / 16.0) - 1,
                                                  fill=fluidColor, outline="")
            else:
                self.f4 = self.c.create_rectangle(0, (7 * height / 16.0) + 1, (7 * width / 16.0) + 1,
                                                  (9 * height / 16.0) - 1,
                                                  fill='black', outline="")
        else:
            xy = [(7 * width / 16.0, 7 * height / 16.0), (7 * width / 16.0, 9 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')

    def setNeighbors(self, top, right, bottom, left):
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left

    def setState(self, fluid):
        self.state = fluid
        if(fluid):
            self.c.itemconfig(self.f0, fill=self.fluidColor)
            if (self.line1):
                self.c.itemconfig(self.f1, fill=self.fluidColor)
            if (self.line2):
                self.c.itemconfig(self.f2, fill=self.fluidColor)
            if (self.line3):
                self.c.itemconfig(self.f3, fill=self.fluidColor)
            if (self.line4):
                self.c.itemconfig(self.f4, fill=self.fluidColor)
        else:
            self.c.itemconfig(self.f0, fill='black')
            if (self.line1):
                self.c.itemconfig(self.f1, fill='black')
            if (self.line2):
                self.c.itemconfig(self.f2, fill='black')
            if (self.line3):
                self.c.itemconfig(self.f3, fill='black')
            if (self.line4):
                self.c.itemconfig(self.f4, fill='black')


    def getState(self):
        return self.state

    def getWidget(self):
        return self.c


#TEST CODE
'''win = tk.Tk()
win.title("ELEMENT TEST")
win.geometry("800x250")
win.configure(bg='black')

s = Pipe(win, 'black', 125, 125, True, True, False, True, '#41d94d', True)
s.getWidget().pack(side='bottom')

win.mainloop()'''