import time
from tkinter import *
from tkinter import colorchooser
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
c = colorchooser.askcolor()
canvas.create_polygon(10, 10, 10, 60, 50, 35, fill=c[1])
for x in range(0, 60):
    canvas.move(1, 5, 5)
    tk.update()
    time.sleep(0.05)
for x in range(0, 60):
    canvas.move(1, -5, -5)
    tk.update()
    time.sleep(0.05)
for x in range(0, 60):
    canvas.move(1, 0, 5)
    tk.update()
    time.sleep(0.05)
for x in range(0, 60):
    canvas.move(1, 0, -5)
    tk.update()
    time.sleep(0.05)
for x in range(0, 60):
    canvas.move(1, 5, 0)
    tk.update()
    time.sleep(0.05)
for x in range(0, 60):
    canvas.move(1, -5, 0)
    tk.update()
    time.sleep(0.05)
