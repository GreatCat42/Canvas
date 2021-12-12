from tkinter import *
from time import sleep

class MAIN:
    def __init__(this):
        #One step from arguments
        this.ROOT = Tk()
        this.MAIN = Canvas(this.ROOT, bg='#222222', width = 400, height = 400)
        this.MAIN.pack()

    def loop(this):
        #The main loop
        while True:
            this.loop_content()
            this.ROOT.update()
            sleep(0.05)

    def line(this,x1,y1,x2,y2):
        #Draws a line
        this.MAIN.create_line(x1,y1,x2,y2,fill='#22cc22')

    def delete(this,target):
        this.MAIN.delete(target)

    def clear(this):
        this.MAIN.delete(ALL)

#This program comes with a strange name... It doesn't matter.
