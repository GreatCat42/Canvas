import sys

sys.path.append('..')

from Tk2050 import MAIN as CANVAS

del sys

from math import sin, cos

canvas = CANVAS()


x=0

def animation():
    global x
    canvas.clear()
    canvas.line(cos(x/30)*10+30,sin(x/30)*10+30,30,30)
    x+=1



canvas.loop_content=animation

canvas.loop()
