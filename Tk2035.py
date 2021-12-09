from tkinter import *
from time import sleep

class MAIN:
    def __init__(this):
        #One step from arguments
        this.ROOT = Tk()
        this.MAIN = Canvas(ROOT, bg='#222222', width = 400, height = 400)
        this.MAIN.pack()

    def loop(this):
        #The main loop
        this.loop_content()
        sleep(0.05)

    def loop_content(this):
        pass



#This program comes with a strange name... It doesn't matter.
