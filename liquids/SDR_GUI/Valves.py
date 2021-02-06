# !/usr/bin/env python3
from tkinter import *

#UNCOMMENT IF TESTING
#import time
#import tkinter as tk


class Solenoid:

    def __init__(self, root, background, num, width, height, line_1, line_2, line_3, line_4, fluidColor):
        self.c = Canvas(root, width=width, height=height, bg=background, highlightthickness=0)
        self.width = width
        self.height = height

        self.inlet = -1
        self.outlet = -1

        self.state = False

        self.fluidColor = fluidColor

        self.fill = self.c.create_rectangle((width/4.0), (height/4.0), (width*(3/4.0)), (height*(3/4.0)), fill='#ab1f1f')
        self.rect = self.c.create_rectangle(width/4.0, height/4.0, width*(3/4.0), height*(3/4.0), outline='white')


        self.l1 = line_1
        self.l2 = line_2
        self.l3 = line_3
        self.l4 = line_4

        self.top = None
        self.right = None
        self.bottom = None
        self.left = None

        #DRAW PIPES
        if(line_1):
            xy = [(7 * width / 16.0, height / 4.0), (7 * width / 16.0, 0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(9 * width / 16.0, height / 4.0), (9 * width / 16.0, 0)]
            self.c.create_line(xy2, width=1, fill='white')
        if(line_2):
            xy = [(width * (3 / 4.0), 7 * height / 16.0), (width, 7 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(width * (3 / 4.0), 9 * height / 16.0), (width, 9 * height / 16.0)]
            self.c.create_line(xy2, width=1, fill='white')
        if(line_3):
            xy = [(7 * width / 16.0, height * (3 / 4.0)), (7 * width / 16.0, height)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(9 * width / 16.0, height * (3 / 4.0)), (9 * width / 16.0, height)]
            self.c.create_line(xy2, width=1, fill='white')
        if(line_4):
            xy = [(width / 4.0, 7 * height / 16.0), (0, 7 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(width / 4.0, 9 * height / 16.0), (0, 9 * height / 16.0)]
            self.c.create_line(xy2, width=1, fill='white')

        #DRAW FLOW
        self.f1 = self.c.create_rectangle((7 * width / 16.0) + 1, 0, (9 * width / 16.0) - 1, (height / 4.0) - 1,
                                                fill='black', outline="")
        self.f2 = self.c.create_rectangle((3 * width / 4.0) + 1, (7 * height / 16.0) + 1, width, (9 * height / 16.0) - 1,
                                              fill='black', outline="")
        self.f3 = self.c.create_rectangle((7 * width / 16.0) + 1, (3 * height / 4.0) + 1, (9 * width / 16.0) - 1, height,
                                              fill='black', outline="")
        self.f4 = self.c.create_rectangle(0, (7 * height / 16.0) + 1, (width / 4.0) - 1, (9 * height / 16.0) - 1,
                                              fill='black', outline="")

        self.c.create_text(width / 2.0, height / 2.0, font=("Arial", 10, 'bold'), fill="white", text=str(num))

    def getWidget(self):
        return self.c

    def setNeighbors(self, top, right, bottom, left):
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left

    def setIn(self, num):
        self.inlet = num

    def setOut(self, num):
        self.outlet = num

    def getState(self):
        return self.state

    def setState(self, open):
        inlet = False
        if (self.inlet == 1):
            if(self.top.getState()):
                self.c.itemconfig(self.f1, fill=self.fluidColor)
                inlet = True
            else:
                self.c.itemconfig(self.f1, fill='black')
        if (self.inlet == 2):
            if(self.right.getState()):
                self.c.itemconfig(self.f2, fill=self.fluidColor)
                inlet = True
            else:
                self.c.itemconfig(self.f2, fill='black')
        if (self.inlet == 3):
            if (self.bottom.getState()):
                self.c.itemconfig(self.f3, fill=self.fluidColor)
                inlet = True
            else:
                self.c.itemconfig(self.f3, fill='black')
        if (self.inlet == 4):
            if (self.left.getState()):
                self.c.itemconfig(self.f4, fill=self.fluidColor)
                inlet = True
            else:
                self.c.itemconfig(self.f4, fill='black')

        if(open):
            self.state = True
            self.c.itemconfig(self.fill, fill='#41d94d')
            if (self.outlet == 1):
                if(inlet):
                    self.c.itemconfig(self.f1, fill=self.fluidColor)
                else:
                    self.c.itemconfig(self.f1, fill='black')
            if (self.outlet == 2):
                if (inlet):
                    self.c.itemconfig(self.f2, fill=self.fluidColor)
                else:
                    self.c.itemconfig(self.f2, fill='black')
            if (self.outlet == 3):
                if (inlet):
                    self.c.itemconfig(self.f3, fill=self.fluidColor)
                else:
                    self.c.itemconfig(self.f3, fill='black')
            if (self.outlet == 4):
                if (inlet):
                    self.c.itemconfig(self.f3, fill=self.fluidColor)
                else:
                    self.c.itemconfig(self.f3, fill='black')
        else:
            self.state = False
            self.c.itemconfig(self.fill, fill = '#ab1f1f')
            if (self.outlet == 1):
                self.c.itemconfig(self.f1, fill='black')
            if (self.outlet == 2):
                self.c.itemconfig(self.f2, fill='black')
            if (self.outlet == 3):
                self.c.itemconfig(self.f3, fill='black')
            if (self.outlet == 4):
                self.c.itemconfig(self.f4, fill='black')




    def setPipes(self, fill_1, fill_2, fill_3, fill_4):
        if (fill_1):
            self.c.itemconfig(self.f1, fill=self.fluidColor)
        else:
            self.c.itemconfig(self.f1, fill='black')
        if (fill_2):
            self.c.itemconfig(self.f2, fill=self.fluidColor)
        else:
            self.c.itemconfig(self.f2, fill='black')
        if (fill_3):
            self.c.itemconfig(self.f3, fill=self.fluidColor)
        else:
            self.c.itemconfig(self.f3, fill='black')
        if (fill_4):
            self.c.itemconfig(self.f4, fill=self.fluidColor)
        else:
            self.c.itemconfig(self.f4, fill='black')

    def getPipes(self):
        return [self.l1, self.l2, self.l3, self.l4]



class Stepper:

    def __init__(self, root, background, width, height, line_1, line_2, line_3, line_4, fluidColor, fill_1, fill_2, fill_3, fill_4):
        self.c = Canvas(root, width=width, height=height, bg=background, highlightthickness=0)
        self.width = width
        self.height = height

        self.fluidColor = fluidColor

        self.fill1 = False
        self.fill2 = False
        self.fill3 = False
        self.fill4 = False

        self.top = None
        self.right = None
        self.bottom = None
        self.left = None

        self.fill = self.c.create_rectangle((width/4.0), (height/4.0), (width*(3/4.0)), (height*(3/4.0)), fill='#ab1f1f')
        self.fillGreen = self.c.create_rectangle((width / 4.0), (height / 4.0), (width / 4.0), (height * (3 / 4.0)), fill='#41d94d')
        self.rect = self.c.create_rectangle(width/4.0, height/4.0, width*(3/4.0), height*(3/4.0), outline='white')

        # DRAW PIPES
        if (line_1):
            xy = [(7 * width / 16.0, height / 4.0), (7 * width / 16.0, 0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(9 * width / 16.0, height / 4.0), (9 * width / 16.0, 0)]
            self.c.create_line(xy2, width=1, fill='white')
        if (line_2):
            xy = [(width * (3 / 4.0), 7 * height / 16.0), (width, 7 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(width * (3 / 4.0), 9 * height / 16.0), (width, 9 * height / 16.0)]
            self.c.create_line(xy2, width=1, fill='white')
        if (line_3):
            xy = [(7 * width / 16.0, height * (3 / 4.0)), (7 * width / 16.0, height)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(9 * width / 16.0, height * (3 / 4.0)), (9 * width / 16.0, height)]
            self.c.create_line(xy2, width=1, fill='white')
        if (line_4):
            xy = [(width / 4.0, 7 * height / 16.0), (0, 7 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(width / 4.0, 9 * height / 16.0), (0, 9 * height / 16.0)]
            self.c.create_line(xy2, width=1, fill='white')

        # DRAW FLOW
        self.f1 = self.c.create_rectangle((7 * width / 16.0) + 1, 0, (9 * width / 16.0) - 1, (height / 4.0) - 1,
                                              fill='black', outline="")
        self.f2 = self.c.create_rectangle((3 * width / 4.0) + 1, (7 * height / 16.0) + 1, width,
                                              (9 * height / 16.0) - 1,
                                              fill='black', outline="")
        self.f3 = self.c.create_rectangle((7 * width / 16.0) + 1, (3 * height / 4.0) + 1, (9 * width / 16.0) - 1,
                                              height,
                                              fill='black', outline="")
        self.f4 = self.c.create_rectangle(0, (7 * height / 16.0) + 1, (width / 4.0) - 1, (9 * height / 16.0) - 1,
                                              fill='black', outline="")

        self.percentage = self.c.create_text(width / 2.0, height / 2.0, font=("Arial", 10, 'bold'), fill="white", text="_ _ %")
        self.per = 0

    def setPipes(self, fill_1, fill_2, fill_3, fill_4):
        self.fill1 = fill_1
        self.fill2 = fill_2
        self.fill3 = fill_3
        self.fill4 = fill_4
        if (fill_1):
            self.c.itemconfig(self.f1, fill=self.fluidColor)
        else:
            self.c.itemconfig(self.f1, fill='black')
        if (fill_2):
            self.c.itemconfig(self.f2, fill=self.fluidColor)
        else:
            self.c.itemconfig(self.f2, fill='black')
        if (fill_3):
            self.c.itemconfig(self.f3, fill=self.fluidColor)
        else:
            self.c.itemconfig(self.f3, fill='black')
        if (fill_4):
            self.c.itemconfig(self.f4, fill=self.fluidColor)
        else:
            self.c.itemconfig(self.f4, fill='black')

    def getPipes(self):
        return [self.fill1, self.fill2, self.fill3, self.fill4]

    def getWidget(self):
        return self.c

    def setNeighbors(self, top, right, bottom, left):
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left

    def setPercentage(self, p):
        self.per = p
        self.c.itemconfig(self.percentage, text=str(p)+' %')
        self.c.coords(self.fillGreen, (self.width / 4.0), (self.height / 4.0), (self.width / 4.0) + ((p/100.0)*self.width/2.0), (self.height * (3 / 4.0)))

    def getPercentage(self):
        return self.per

class Orifice:

    def __init__(self, root, background, width, height, line_1, line_2, line_3, line_4, fluidColor, fill_1, fill_2, fill_3, fill_4):
        self.c = Canvas(root, width=width, height=height, bg=background, highlightthickness=0)
        self.width = width
        self.height = height

        self.fluidColor = fluidColor

        self.state = False

        self.line_1 = line_1
        self.line_2 = line_2
        self.line_3 = line_3
        self.line_4 = line_4

        self.top = None
        self.right = None
        self.bottom = None
        self.left = None

        self.rect = self.c.create_rectangle(width/4.0, height/4.0, width*(3/4.0), height*(3/4.0), outline='white')
        self.c.create_line((width / 4.0, height / 2.0), (3 * width / 4.0, height / 2.0), width=1, fill='white')
        self.beforeP = self.c.create_text(width / 2.0, 3 * height / 8.0, font=("Arial", 8, 'bold'), fill="white",
                                             text="B: __ Pa")
        self.afterP = self.c.create_text(width / 2.0, 5 * height / 8.0, font=("Arial", 8, 'bold'), fill="white",
                                         text="A: __ Pa")
        self.name = self.c.create_text(width/4.0, height/8.0, font=("Arial", 6, 'bold'), fill="white",
                                         text="Orifice")

        #DRAW PIPES
        if(line_1):
            xy = [(7 * width / 16.0, height / 4.0), (7 * width / 16.0, 0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(9 * width / 16.0, height / 4.0), (9 * width / 16.0, 0)]
            self.c.create_line(xy2, width=1, fill='white')
        if(line_2):
            xy = [(width * (3 / 4.0), 7 * height / 16.0), (width, 7 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(width * (3 / 4.0), 9 * height / 16.0), (width, 9 * height / 16.0)]
            self.c.create_line(xy2, width=1, fill='white')
        if(line_3):
            xy = [(7 * width / 16.0, height * (3 / 4.0)), (7 * width / 16.0, height)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(9 * width / 16.0, height * (3 / 4.0)), (9 * width / 16.0, height)]
            self.c.create_line(xy2, width=1, fill='white')
        if(line_4):
            xy = [(width / 4.0, 7 * height / 16.0), (0, 7 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(width / 4.0, 9 * height / 16.0), (0, 9 * height / 16.0)]
            self.c.create_line(xy2, width=1, fill='white')

        #DRAW FLOW
        self.f1 = self.c.create_rectangle((7 * width / 16.0) + 1, 0, (9 * width / 16.0) - 1, (height / 4.0) - 1,
                                          fill='black', outline="")
        self.f2 = self.c.create_rectangle((3 * width / 4.0) + 1, (7 * height / 16.0) + 1, width,
                                          (9 * height / 16.0) - 1,
                                          fill='black', outline="")
        self.f3 = self.c.create_rectangle((7 * width / 16.0) + 1, (3 * height / 4.0) + 1, (9 * width / 16.0) - 1,
                                          height,
                                          fill='black', outline="")
        self.f4 = self.c.create_rectangle(0, (7 * height / 16.0) + 1, (width / 4.0) - 1, (9 * height / 16.0) - 1,
                                          fill='black', outline="")

    def setPipes(self, state):
        self.state = state
        if(state):
            if (self.line_1):
                self.c.itemconfig(self.f1, fill=self.fluidColor)
            if (self.line_2):
                self.c.itemconfig(self.f2, fill=self.fluidColor)
            if (self.line_3):
                self.c.itemconfig(self.f3, fill=self.fluidColor)
            if (self.line_4):
                self.c.itemconfig(self.f4, fill=self.fluidColor)
        else:
            if (self.line_1):
                self.c.itemconfig(self.f1, fill='black')
            if (self.line_2):
                self.c.itemconfig(self.f2, fill='black')
            if (self.line_3):
                self.c.itemconfig(self.f3, fill='black')
            if (self.line_4):
                self.c.itemconfig(self.f4, fill='black')

    def getState(self):
        return self.state

    def getPipes(self):
        return [self.l1, self.l2, self.l3, self.l4]


    def getWidget(self):
        return self.c

    def setValues(self, before, after):
        self.c.itemconfig(self.beforeP, text='B: ' + before + ' Pa')
        self.c.itemconfig(self.afterP, text='A: ' + after + ' Pa')

    def setNeighbors(self, top, right, bottom, left):
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left

class PressureSensor:

    def __init__(self, root, background, width, height, line_1, line_2, line_3, line_4, fluidColor, fill_1, fill_2, fill_3, fill_4):
        self.c = Canvas(root, width=width, height=height, bg=background, highlightthickness=0)
        self.width = width
        self.height = height

        self.line_1 = line_1
        self.line_2 = line_2
        self.line_3 = line_3
        self.line_4 = line_4

        self.fluidColor = fluidColor

        self.state = False

        self.top = None
        self.right = None
        self.bottom = None
        self.left = None

        self.rect = self.c.create_oval(width / 4.0, height / 4.0, width * (3 / 4.0), height * (3 / 4.0),
                                            outline='white', width=1)
        self.p = self.c.create_text(width / 2.0, height / 2.0, font=("Arial", 8, 'bold'), fill="white",
                                             text="__ Pa")
        self.name = self.c.create_text(width/4.0, height/8.0, font=("Arial", 6, 'bold'), fill="white",
                                         text="Pressure\nSensor")

        #DRAW PIPES
        if(line_1):
            xy = [(7 * width / 16.0, height / 4.0), (7 * width / 16.0, 0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(9 * width / 16.0, height / 4.0), (9 * width / 16.0, 0)]
            self.c.create_line(xy2, width=1, fill='white')
        if(line_2):
            xy = [(width * (3 / 4.0), 7 * height / 16.0), (width, 7 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(width * (3 / 4.0), 9 * height / 16.0), (width, 9 * height / 16.0)]
            self.c.create_line(xy2, width=1, fill='white')
        if(line_3):
            xy = [(7 * width / 16.0, height * (3 / 4.0)), (7 * width / 16.0, height)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(9 * width / 16.0, height * (3 / 4.0)), (9 * width / 16.0, height)]
            self.c.create_line(xy2, width=1, fill='white')
        if(line_4):
            xy = [(width / 4.0, 7 * height / 16.0), (0, 7 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(width / 4.0, 9 * height / 16.0), (0, 9 * height / 16.0)]
            self.c.create_line(xy2, width=1, fill='white')

        #DRAW FLOW
        self.f1 = self.c.create_rectangle((7 * width / 16.0) + 1, 0, (9 * width / 16.0) - 1, (height / 4.0) - 1,
                                          fill='black', outline="")
        self.f2 = self.c.create_rectangle((3 * width / 4.0) + 1, (7 * height / 16.0) + 1, width,
                                          (9 * height / 16.0) - 1,
                                          fill='black', outline="")
        self.f3 = self.c.create_rectangle((7 * width / 16.0) + 1, (3 * height / 4.0) + 1, (9 * width / 16.0) - 1,
                                          height,
                                          fill='black', outline="")
        self.f4 = self.c.create_rectangle(0, (7 * height / 16.0) + 1, (width / 4.0) - 1, (9 * height / 16.0) - 1,
                                          fill='black', outline="")


    def getWidget(self):
        return self.c

    def setPipes(self, state):
        self.state = state
        if(state):
            if (self.line_1):
                self.c.itemconfig(self.f1, fill=self.fluidColor)
            if (self.line_2):
                self.c.itemconfig(self.f2, fill=self.fluidColor)
            if (self.line_3):
                self.c.itemconfig(self.f3, fill=self.fluidColor)
            if (self.line_4):
                self.c.itemconfig(self.f4, fill=self.fluidColor)
        else:
            if (self.line_1):
                self.c.itemconfig(self.f1, fill='black')
            if (self.line_2):
                self.c.itemconfig(self.f2, fill='black')
            if (self.line_3):
                self.c.itemconfig(self.f3, fill='black')
            if (self.line_4):
                self.c.itemconfig(self.f4, fill='black')

    def getState(self):
        return self.state

    def setNeighbors(self, top, right, bottom, left):
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left

    def setValues(self, pressure):
        self.c.itemconfig(self.p, text=pressure)

class TempSensor:

    def __init__(self, root, background, width, height, line_1, line_2, line_3, line_4, fluidColor, fill_1, fill_2, fill_3, fill_4):
        self.c = Canvas(root, width=width, height=height, bg=background, highlightthickness=0)
        self.width = width
        self.height = height

        self.line_1 = line_1
        self.line_2 = line_2
        self.line_3 = line_3
        self.line_4 = line_4

        self.state = False

        self.fluidColor = fluidColor

        self.top = None
        self.right = None
        self.bottom = None
        self.left = None

        self.rect = self.c.create_oval(width / 4.0, height / 4.0, width * (3 / 4.0), height * (3 / 4.0),
                                            outline='white', width=1)
        self.p = self.c.create_text(width / 2.0, height / 2.0, font=("Arial", 8, 'bold'), fill="white",
                                             text="__ °C")
        self.name = self.c.create_text(width/4.0, height/8.0, font=("Arial", 6, 'bold'), fill="white",
                                         text="Temp\nSensor")

        #DRAW PIPES
        if(line_1):
            xy = [(7 * width / 16.0, height / 4.0), (7 * width / 16.0, 0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(9 * width / 16.0, height / 4.0), (9 * width / 16.0, 0)]
            self.c.create_line(xy2, width=1, fill='white')
        if(line_2):
            xy = [(width * (3 / 4.0), 7 * height / 16.0), (width, 7 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(width * (3 / 4.0), 9 * height / 16.0), (width, 9 * height / 16.0)]
            self.c.create_line(xy2, width=1, fill='white')
        if(line_3):
            xy = [(7 * width / 16.0, height * (3 / 4.0)), (7 * width / 16.0, height)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(9 * width / 16.0, height * (3 / 4.0)), (9 * width / 16.0, height)]
            self.c.create_line(xy2, width=1, fill='white')
        if(line_4):
            xy = [(width / 4.0, 7 * height / 16.0), (0, 7 * height / 16.0)]
            self.c.create_line(xy, width=1, fill='white')
            xy2 = [(width / 4.0, 9 * height / 16.0), (0, 9 * height / 16.0)]
            self.c.create_line(xy2, width=1, fill='white')

        #DRAW FLOW
        self.f1 = self.c.create_rectangle((7 * width / 16.0) + 1, 0, (9 * width / 16.0) - 1, (height / 4.0) - 1,
                                          fill='black', outline="")
        self.f2 = self.c.create_rectangle((3 * width / 4.0) + 1, (7 * height / 16.0) + 1, width,
                                          (9 * height / 16.0) - 1,
                                          fill='black', outline="")
        self.f3 = self.c.create_rectangle((7 * width / 16.0) + 1, (3 * height / 4.0) + 1, (9 * width / 16.0) - 1,
                                          height,
                                          fill='black', outline="")
        self.f4 = self.c.create_rectangle(0, (7 * height / 16.0) + 1, (width / 4.0) - 1, (9 * height / 16.0) - 1,
                                          fill='black', outline="")


    def getWidget(self):
        return self.c

    def setPipes(self, state):
        self.state = state
        if(state):
            if (self.line_1):
                self.c.itemconfig(self.f1, fill=self.fluidColor)
            if (self.line_2):
                self.c.itemconfig(self.f2, fill=self.fluidColor)
            if (self.line_3):
                self.c.itemconfig(self.f3, fill=self.fluidColor)
            if (self.line_4):
                self.c.itemconfig(self.f4, fill=self.fluidColor)
        else:
            if (self.line_1):
                self.c.itemconfig(self.f1, fill='black')
            if (self.line_2):
                self.c.itemconfig(self.f2, fill='black')
            if (self.line_3):
                self.c.itemconfig(self.f3, fill='black')
            if (self.line_4):
                self.c.itemconfig(self.f4, fill='black')

    def getState(self):
        return self.state

    def setNeighbors(self, top, right, bottom, left):
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left

    def setValues(self, pressure):
        self.c.itemconfig(self.p, text=pressure)

#TEST CODE
'''win = tk.Tk()
win.title("ELEMENT TEST")
win.geometry("800x375")
win.configure(bg='black')

s = Solenoid(win, 'black', 1, 125, 125, True, True, True, True, '#41d94d', True, True, True, True)
s.getWidget().pack(side='bottom')
st = Stepper(win, 'black', 125, 125, True, True, True, True, '#41d94d', True, True, True, True)
st.getWidget().pack(side='top')
o = PressureSensor(win, 'black', 125, 125, True, True, True, True, '#41d94d', True, True, True, True)
o.getWidget().pack(side='top')

while True:
    s.setState(True)
    win.update()
    time.sleep(1)
    s.setState(False)
    win.update()
    time.sleep(1)
    for i in range(101):
        st.setPercentage(i)
        time.sleep(0.01)
        win.update()


win.mainloop()'''