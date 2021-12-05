#!/usr/bin/python
# -*- coding: UTF-8 -*-

from time import sleep
 
#import tkinter
# 创建一个矩形，指定画布的颜色为白色
from tkinter import *
root = Tk()
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root,bg = 'black',width=800,height=400)
# 创建一个矩形，坐标为(10,10,110,110)

cv.pack()
a=cv.create_rectangle(20,20,40,40,fill='green')

while True:
    sleep(0.05)
    cv.move(a,1,0)
    root.update()


print('AIEEE!')


# 为明显起见，将背景色设置为白色，用以区别 root
