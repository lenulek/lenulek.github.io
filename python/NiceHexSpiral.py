# NiceHexSpiral.py
import turtle
colors=['purple', 'red', 'cyan', 'seashell', 'gold', 'magenta', 'blue', 'yellow', 'white', 'orange','green', 'pink']
#colors=['purple', 'red', 'cyan', '#eed8ae']
t = turtle.Pen()
t.shape('turtle')
t.speed(0)
tina = turtle.Turtle()
tina.shape('circle')
tina.speed(0)

turtle.bgcolor('black')

for x in range (360):
    t.pencolor(colors[x%len(colors)])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)
    angle = 360 / len(colors)
    tina.color(colors[x%len(colors)])
    tina.circle(x/3)
    tina.right(angle)
    tina.forward(30)
  
