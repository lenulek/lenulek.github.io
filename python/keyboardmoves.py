#import all neccessary modules
import time
from tkinter import *
from tkinter import colorchooser

#create tkinter window
tk = Tk()

#choose color for background
b = colorchooser.askcolor()
canvas = Canvas(tk, bg=b[1], width=400, height=400)
canvas.pack()

#choose color for triangle
c = colorchooser.askcolor()
canvas.create_polygon(10, 10, 10, 60, 50, 35, fill=c[1])

#function to move triangle from keyboard
def movetriangle(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -3)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 3)
    elif event.keysym == 'Left':
        canvas.move(1, -3, 0)
    else:
        canvas.move(1, 3, 0)
canvas.bind_all('<KeyPress-Up>', movetriangle)
canvas.bind_all('<KeyPress-Down>', movetriangle)
canvas.bind_all('<KeyPress-Left>', movetriangle)
canvas.bind_all('<KeyPress-Right>', movetriangle)
