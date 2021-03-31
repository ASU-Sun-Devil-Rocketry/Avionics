import tkinter as tk

import Nozzle
import Tank
import Valves
import Pipes
import Header


class Liquid_Engine_Plumbing:

    def __init__(self, gridLen):

        width = gridLen * 8
        height = gridLen * 12

        self.win = tk.Tk()
        self.win.title("P&ID Diagram")
        self.win.geometry(str(width) + "x" + str(height))
        self.win.configure(bg='black')

        # CONSTANT
        fluidColor = '#41d94d'

        # HEADER
        self.header = Header.Header(self.win, 'black', 'SDR P&ID GUI', width, gridLen, 24)
        self.header.getWidget().place(x=gridLen * 0, y=gridLen * 0)

        # All TANKS
        self.gn2 = Tank.Tank(self.win, 'black', 'GN2', '#1d2396', gridLen, gridLen)
        self.lox = Tank.Tank(self.win, 'black', 'LOx', '#1d2396', gridLen, gridLen)
        self.k = Tank.Tank(self.win, 'black', 'K', '#1d2396', gridLen, gridLen)
        self.gn2.getWidget().place(x=gridLen * 3, y=gridLen * 1)
        self.lox.getWidget().place(x=gridLen * 1, y=gridLen * 5)
        self.k.getWidget().place(x=gridLen * 6, y=gridLen * 5)

        # All SOLENOID VALVES
        self.one = Valves.Solenoid(self.win, 'black', 1, gridLen, gridLen, False, True, True, False, fluidColor)
        self.two = Valves.Solenoid(self.win, 'black', 2, gridLen, gridLen, False, True, False, False, fluidColor)
        self.three = Valves.Solenoid(self.win, 'black', 3, gridLen, gridLen, False, False, True, True, fluidColor)
        self.four = Valves.Solenoid(self.win, 'black', 4, gridLen, gridLen, False, True, False, False, fluidColor)
        self.five = Valves.Solenoid(self.win, 'black', 5, gridLen, gridLen, True, False, False, True, fluidColor)
        self.six = Valves.Solenoid(self.win, 'black', 6, gridLen, gridLen, False, True, False, True, fluidColor)
        self.one.getWidget().place(x=gridLen * 1, y=gridLen * 2)
        self.one.setIn(2)
        self.one.setOut(3)
        self.two.getWidget().place(x=gridLen * 0, y=gridLen * 4)
        self.two.setIn(2)
        self.three.getWidget().place(x=gridLen * 6, y=gridLen * 2)
        self.three.setIn(4)
        self.three.setOut(3)
        self.four.getWidget().place(x=gridLen * 5, y=gridLen * 4)
        self.four.setIn(2)
        self.five.getWidget().place(x=gridLen * 3, y=gridLen * 8)
        self.five.setIn(1)
        self.five.setOut(4)
        self.six.getWidget().place(x=gridLen * 4, y=gridLen * 7)
        self.six.setIn(4)
        self.six.setOut(2)

        # All STEPPER
        self.s1 = Valves.Stepper(self.win, 'black', gridLen, gridLen, True, False, False, True, '#41d94d', False, False, False,
                            False)
        self.s2 = Valves.Stepper(self.win, 'black', gridLen, gridLen, False, True, True, True, '#41d94d', False, False, False,
                            False)
        self.s1.getWidget().place(x=gridLen * 6, y=gridLen * 7)
        self.s2.getWidget().place(x=gridLen * 2, y=gridLen * 8)

        # All ORIFICES
        self.o1 = Valves.Orifice(self.win, 'black', gridLen, gridLen, True, False, True, False, '#41d94d', False, False, False,
                            False)
        self.o2 = Valves.Orifice(self.win, 'black', gridLen, gridLen, False, True, True, True, '#41d94d', False, False, False,
                            False)
        self.o1.getWidget().place(x=gridLen * 1, y=gridLen * 6)
        self.o2.getWidget().place(x=gridLen * 5, y=gridLen * 7)

        # All Pressure Sensors
        self.ps1 = Valves.PressureSensor(self.win, 'black', gridLen, gridLen, False, True, False, False, '#41d94d', False, False,
                                    False, False)
        self.ps2 = Valves.PressureSensor(self.win, 'black', gridLen, gridLen, False, True, True, True, '#41d94d', False, False,
                                    False,
                                    False)
        self.ps3 = Valves.PressureSensor(self.win, 'black', gridLen, gridLen, False, False, False, True, '#41d94d', False, False,
                                    False, False)
        self.ps1.getWidget().place(x=gridLen * 0, y=gridLen * 3)
        self.ps2.getWidget().place(x=gridLen * 5, y=gridLen * 9)
        self.ps3.getWidget().place(x=gridLen * 7, y=gridLen * 3)

        self.tp1 = Valves.TempSensor(self.win, 'black', gridLen, gridLen, True, False, False, False, '#41d94d', False, False,
                                False,
                                False)
        self.tp1.getWidget().place(x=gridLen * 5, y=gridLen * 10)

        # All Text boxes
        self.t1 = Header.Text(self.win, 'black', 'K Fill', gridLen, gridLen, 12)
        self.t2 = Header.Text(self.win, 'black', 'K Drain', gridLen, gridLen, 12)
        self.t3 = Header.Text(self.win, 'black', 'LOx\nFill/Drain', gridLen, gridLen, 12)
        self.t4 = Header.Text(self.win, 'black', 'Regen\nCircuit', gridLen, gridLen, 12)
        self.t1.getWidget().place(x=gridLen * 7, y=gridLen * 4)
        self.t2.getWidget().place(x=gridLen * 7, y=gridLen * 6)
        self.t3.getWidget().place(x=gridLen * 1, y=gridLen * 9)
        self.t4.getWidget().place(x=gridLen * 7, y=gridLen * 9)

        # All PIPES
        self.p1 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, False, True, False, True, '#41d94d', False)
        self.p2 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, True, True, True, '#41d94d', False)
        self.p3 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, False, True, False, True, '#41d94d', False)
        self.p4 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, False, True, False, True, '#41d94d', False)
        self.p5 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, False, True, True, '#41d94d', False)
        self.p6 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, False, True, False, '#41d94d', False)
        self.p7 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, True, True, False, '#41d94d', False)
        self.p8 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, False, True, True, '#41d94d', False)
        self.p9 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, False, True, False, '#41d94d', False)
        self.p10 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, True, True, True, '#41d94d', False)
        self.p11 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, False, True, False, '#41d94d', False)
        self.p12 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, False, True, False, '#41d94d', False)
        self.p13 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, True, True, False, '#41d94d', False)
        self.p14 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, False, True, False, '#41d94d', False)
        self.p15 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, True, True, False, '#41d94d', False)
        self.p16 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, True, True, False, '#41d94d', False)
        self.p17 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, True, False, False, '#41d94d', False)
        self.p18 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, False, False, True, True, '#41d94d', False)
        self.p19 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, True, False, False, '#41d94d', False)
        self.p20 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, False, True, True, True, '#41d94d', False)
        self.p21 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, False, True, False, True, '#41d94d', False)
        self.p22 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, False, False, True, '#41d94d', False)
        self.p1.getWidget().place(x=gridLen * 2, y=gridLen * 2)
        self.p2.getWidget().place(x=gridLen * 3, y=gridLen * 2)
        self.p3.getWidget().place(x=gridLen * 4, y=gridLen * 2)
        self.p4.getWidget().place(x=gridLen * 5, y=gridLen * 2)
        self.p5.getWidget().place(x=gridLen * 1, y=gridLen * 3)
        self.p6.getWidget().place(x=gridLen * 3, y=gridLen * 3)
        self.p7.getWidget().place(x=gridLen * 6, y=gridLen * 3)
        self.p8.getWidget().place(x=gridLen * 1, y=gridLen * 4)
        self.p9.getWidget().place(x=gridLen * 3, y=gridLen * 4)
        self.p10.getWidget().place(x=gridLen * 6, y=gridLen * 4)
        self.p11.getWidget().place(x=gridLen * 3, y=gridLen * 5)
        self.p12.getWidget().place(x=gridLen * 3, y=gridLen * 6)
        self.p13.getWidget().place(x=gridLen * 6, y=gridLen * 6)
        self.p14.getWidget().place(x=gridLen * 1, y=gridLen * 7)
        self.p15.getWidget().place(x=gridLen * 3, y=gridLen * 7)
        self.p16.getWidget().place(x=gridLen * 1, y=gridLen * 8)
        self.p17.getWidget().place(x=gridLen * 5, y=gridLen * 8)
        self.p18.getWidget().place(x=gridLen * 6, y=gridLen * 8)
        self.p19.getWidget().place(x=gridLen * 2, y=gridLen * 9)
        self.p20.getWidget().place(x=gridLen * 3, y=gridLen * 9)
        self.p21.getWidget().place(x=gridLen * 4, y=gridLen * 9)
        self.p22.getWidget().place(x=gridLen * 6, y=gridLen * 9)

        # NOZZLE
        self.n = Nozzle.Nozzle(self.win, 'black', gridLen, gridLen * 1.5)
        self.n.getWidget().place(x=gridLen * 3, y=gridLen * 10)

        #self.s2.setNeighbors(None, self.five, self.p19, self.p16)
        #self.s1.setNeighbors(self.p13, None, None, self.o2)


        #SET ALL VIRTUAL COMPONENTS (linked list)
        self.head = self.gn2
        #row 1
        self.gn2.setNeighbors(None, None, self.p2, None)
        #row 2
        self.one.setNeighbors(None, self.p1, self.p5, None)
        self.p1.setNeighbors(None, self.p2, None, self.one)
        self.p2.setNeighbors(self.gn2, self.p3, self.p6, self.p1)
        self.p3.setNeighbors(None, self.p4, None, self.p2)
        self.p4.setNeighbors(None, self.three, None, self.p3)
        self.three.setNeighbors(None, None, self.p7, self.p4)
        #row 3
        self.ps1.setNeighbors(None, self.p5, None, None)
        self.p5.setNeighbors(self.one, None, self.p8, self.ps1)
        self.p6.setNeighbors(self.p2, None, self.p9, None)
        self.p7.setNeighbors(self.three, self.ps2, self.p10, None)
        self.ps2.setNeighbors(None, None, None, self.p7)
        #row 4
        self.two.setNeighbors(None, self.p8, None, None)
        self.p8.setNeighbors(self.p5, None, self.lox, self.two)
        self.p9.setNeighbors(self.p6, None, self.p11, None)
        self.four.setNeighbors(None, self.p10, None, None)
        self.p10.setNeighbors(self.p7, None, self.k, self.four)
        #row5
        self.lox.setNeighbors(self.p8, None, self.o1, None)
        self.p11.setNeighbors(self.p9, None, self.p12, None)
        self.k.setNeighbors(self.p10, None, self.p13, None)
        #row 6
        self.o1.setNeighbors(self.lox, None, self.p14, None)
        self.p12.setNeighbors(self.p11, None, self.p15, None)
        self.p13.setNeighbors(self.k, None, self.s1, None)
        #row 7
        self.p14.setNeighbors(self.o1, None, self.p16, None)
        self.p15.setNeighbors(self.p12, self.six, self.five, None)
        self.six.setNeighbors(None, self.o2, None, self.p15)
        self.o2.setNeighbors(None, self.s1, self.p17, self.six)
        self.s1.setNeighbors(self.p13, None, None, self.o2)
        #row 8
        self.p16.setNeighbors(self.p14, self.s2, None, None)
        self.s2.setNeighbors(None, self.five, self.p19, self.p16)
        self.five.setNeighbors(self.p15, None, None, self.s2)
        self.p17.setNeighbors(self.o2, self.p18, None, None)
        self.p18.setNeighbors(None, None, self.p22, self.p17)
        #row 9
        self.p19.setNeighbors(self.s2, self.p20, None, None)
        self.p20.setNeighbors(None, self.p21, self.n, self.p19)
        self.p21.setNeighbors(None, self.ps3, None, self.p20)
        self.ps3.setNeighbors(None, self.p22, self.tp1, self.p21)
        self.p22.setNeighbors(self.p18, None, None, self.ps3)
        #row 10
        self.n.setNeighbors(self.p20, None, None, None)
        self.tp1.setNeighbors(self.ps3, None, None, None)


    def getHead(self):
        return self.gn2

    def updatePipeStatus(self):
        head = self.getHead()
        prvHead = None

        listMultiplePaths = []
        while(head is not Nozzle.Nozzle):
            num = 0
            print(type(head))
            if (type(head) is Pipes.Pipe):
                head.setState(True)
            if(head is None):
                print("DONE")
                break
            if(type(head) is Valves.Solenoid and not head.getState()):
                if(type(head.right) is Pipes.Pipe and head.right.getState()):
                    head.setPipes(False, True, False, False)
                if(type(head.left) is Pipes.Pipe and head.left.getState()):
                    head.setPipes(False, False, False, True)
                break

            if(head.left is not None):
                num+=1
            if(head.right is not None):
                num+=1
            if(head.bottom is not None):
                num+=1

            if(num >= 2):
                listMultiplePaths.append(head)

            if(head.left is not None and head.left != prvHead):
                print("Left " + str(type(head.left)))
                print("Prv Head: " + str(type(prvHead)))
                prvHead = head
                head = head.left
            elif(head.bottom is not None and head.bottom != prvHead):
                print("Bottom " + str(type(head.bottom)))
                print("Prv Head: " + str(type(prvHead)))
                prvHead = head
                head = head.bottom
            elif(head.right is not None and head.right != prvHead):
                print("Right " + str(type(head.right)))
                print("Prv Head: " + str(type(prvHead)))
                prvHead = head
                head = head.right
            else:
                print("DONE")
                break

    def getWindow(self):
        return self.win


class Solids_Engine_Plumbing:

    def __init__(self, gridLen):

        width = gridLen * 3
        height = gridLen * 7

        self.win = tk.Tk()
        self.win.title("P&ID Diagram")
        self.win.geometry(str(width) + "x" + str(height))
        self.win.configure(bg='black')

        # CONSTANT
        fluidColor = '#41d94d'

        # HEADER
        self.header = Header.Header(self.win, 'black', 'P&ID', width, gridLen, 24)
        self.header.getWidget().place(x=gridLen * 0, y=gridLen * 0)

        # All TANKS
        self.gn2 = Tank.Tank(self.win, 'black', 'GN2', '#1d2396', gridLen, gridLen)
        self.ovp = Tank.Tank(self.win, 'black', 'Over\nPres', '#f542b9', gridLen, gridLen)
        self.gn2.getWidget().place(x=gridLen * 0, y=gridLen * 1)
        self.ovp.getWidget().place(x=gridLen * 2, y=gridLen * 1)

        # All SOLENOID VALVES
        self.one = Valves.Solenoid(self.win, 'black', 1, gridLen, gridLen, True, False, True, False, fluidColor)
        self.two = Valves.Solenoid(self.win, 'black', 1, gridLen, gridLen, True, False, True, False, fluidColor)
        self.one.getWidget().place(x=gridLen * 0, y=gridLen * 2)
        self.two.getWidget().place(x=gridLen * 2, y=gridLen * 2)

        # All Pressure Sensors
        self.ps1 = Valves.PressureSensor(self.win, 'black', gridLen, gridLen, False, False, False, True, '#41d94d', False, False, False, False)
        self.ps1.getWidget().place(x=gridLen * 2, y=gridLen * 4)

        # All Text boxes
        self.t1 = Header.Text(self.win, 'black', 'Relief Valve', gridLen, gridLen, 12)
        self.t2 = Header.Text(self.win, 'black', 'WIRE 1', gridLen, gridLen, 12)
        self.t3 = Header.Text(self.win, 'black', 'WIRE 2', gridLen, gridLen, 12)
        self.t1.getWidget().place(x=gridLen * 0, y=gridLen * 4)
        self.t2.getWidget().place(x=gridLen * 2, y=gridLen * 5)
        self.t3.getWidget().place(x=gridLen * 2, y=gridLen * 6)

        # All PIPES
        self.p1 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, True, False, False, '#41d94d', False)
        self.p2 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, False, True, True, True, '#41d94d', False)
        self.p3 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, False, False, True, '#41d94d', False)
        self.p4 = Pipes.Pipe(self.win, 'black', gridLen, gridLen, True, True, True, True, '#41d94d', False)
        self.p1.getWidget().place(x=gridLen * 0, y=gridLen * 3)
        self.p2.getWidget().place(x=gridLen * 1, y=gridLen * 3)
        self.p3.getWidget().place(x=gridLen * 2, y=gridLen * 3)
        self.p4.getWidget().place(x=gridLen * 1, y=gridLen * 4)


        # NOZZLE
        self.n = Nozzle.Nozzle(self.win, 'black', gridLen, gridLen * 1.5)
        self.n.getWidget().place(x=gridLen * 1, y=gridLen * 5)



    def getWindow(self):
        return self.win