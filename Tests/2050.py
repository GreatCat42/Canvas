import sys

sys.path.append('..')

from Tk2050 import *

del sys

from math import sin, cos


x=0

def draw():
    global x
    x+=0.3
    clear()
    line(cos(x/30)*10+30,sin(x/30)*10+30,30,30)

from Tk2050 import loop

loop()
