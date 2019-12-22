import time
from tkinter import *
from tkinter import colorchooser
import random
tk = Tk()
b = colorchooser.askcolor()
canvas = Canvas(tk, bg=b[1], width=400, height=400)
canvas.pack()
c = colorchooser.askcolor()
d = colorchooser.askcolor()
def random_triangle_1(leg):
    x1 = random.randrange(leg)
    y1 = x1
    x2 = x1 + random.randrange(leg)
    y2 = y1 + random.randrange(leg)
    canvas.create_polygon(x1, y1, x2, y1, x2, y2, fill="",outline=c[1])
def random_triangle_2(leg):
    x1 = random.randrange(leg)
    y1 = x1
    x2 = x1 + random.randrange(leg)
    y2 = y1 + random.randrange(leg)
    y3 = y1 + random.randrange(leg)
    canvas.create_polygon(x1, y1, x1, y2, x2, y3, fill="",outline=d[1])
for x in range(0, 50):
    random_triangle_1(250)
    random_triangle_2(150)

