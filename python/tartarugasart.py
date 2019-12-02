# le mie tartaruge piccole

import turtle

colors=['purple', 'red', 'cyan', 'seashell', 'gold', 'magenta', 'blue', 'yellow', 'white', 'orange','green', 'pink']

aica = turtle.Pen()
aica.shape('turtle')
aica.speed(0)

bina = turtle.Turtle()
bina.shape('turtle')
bina.speed(0)

cfex = turtle.Pen()
cfex.shape('turtle')
cfex.speed(0)

doxy = turtle.Turtle()
doxy.shape('turtle')
doxy.speed(0)

eta = turtle.Turtle()
eta.shape('turtle')
eta.speed(0)

ina = turtle.Turtle()
ina.shape('turtle')
ina.speed(0)

z = turtle.Turtle()
z.shape('turtle')
z.speed(0)

lee = turtle.Pen()
lee.shape('turtle')
lee.speed(0)

aica.left(45)
bina.left(90)
cfex.left(135)
doxy.left(180)
eta.left(225)
ina.left(270)
z.left(315)

turtle.bgcolor('black')

aica.forward(100)
bina.forward(100)
cfex.forward(100)
doxy.forward(100)
eta.forward(100)
ina.forward(100)
z.forward(100)
lee.forward(100)

for x in range (160):
    aica.pencolor(colors[x%len(colors)])
    aica.width(x/100+1)
    aica.forward(x)
    aica.left(59)
    angle = 360 / len(colors)

    bina.pencolor(colors[x%len(colors)])
    bina.width(x/100+1)
    bina.forward(x)
    bina.left(59)
    angle = 360 / len(colors)

    cfex.pencolor(colors[x%len(colors)])
    cfex.width(x/100+1)
    cfex.forward(x)
    cfex.left(59)
    angle = 360 / len(colors)

    doxy.pencolor(colors[x%len(colors)])
    doxy.width(x/100+1)
    doxy.forward(x)
    doxy.left(59)
    angle = 360 / len(colors)

    eta.pencolor(colors[x%len(colors)])
    eta.width(x/100+1)
    eta.forward(x)
    eta.left(59)
    angle = 360 / len(colors)

    ina.pencolor(colors[x%len(colors)])
    ina.width(x/100+1)
    ina.forward(x)
    ina.left(59)
    angle = 360 / len(colors)

    z.pencolor(colors[x%len(colors)])
    z.width(x/100+1)
    z.forward(x)
    z.left(59)
    angle = 360 / len(colors)

    lee.pencolor(colors[x%len(colors)])
    lee.width(x/100+1)
    lee.forward(x)
    lee.left(59)
    angle = 360 / len(colors)
    #ina.color(colors[x%len(colors)])
    #ina.circle(x/3)
    #ina.right(angle)
    #ina.forward(30)
  
