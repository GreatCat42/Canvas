from tkinter import *

win = Tk()
win.geometry('500x500+500+100')
canvas = Canvas(win)
canvas.pack(fill=BOTH, expand=True)
# Draws an awkward pentagon, fill pink
point = [(50, 50), (100, 50), (100, 100), (75, 150), (50, 100)]
canvas.create_polygon(point, fill='pink', width=5, outline='orange')
win.mainloop()
