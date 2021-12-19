from time import sleep


from tkinter import *

#Create the Root Window
root = Tk()

#Create the Canvas
cv = Canvas(root,bg = '#222222',width=800,height=400)

#We're all in it together!
cv.pack()

# Create this green rectangle
a=cv.create_rectangle(20,20,40,40,fill='#42d242')

# Here we are, entering the 'draw=function'
while True:
    sleep(0.05)
    cv.move(a,1,0)
    root.update()
