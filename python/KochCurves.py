##рисование линий Коха
import turtle

##print(turtle.position())

t = turtle.Pen()
t.speed(0)
t.up()
t.goto(-300,200)
t.down()
turtle.bgcolor('black')
t.color('cyan')

l=90
a=60
for x in range(11):
    t.forward(l/3)
    t.left(a)
    t.forward(l/3)
    t.left(300-a)
    t.forward(l/3)
    t.left(a)

t.up()
t.goto(-300,100)
t.down()

for x in range(11):
    t.forward((l/3)/3)
    t.left(a)
    t.forward((l/3)/3)
    t.left(300-a)
    t.forward((l/3)/3)
    t.left(a)
    t.forward((l/3)/3)
    t.left(a)
    t.forward((l/3)/3)
    t.left(a)
    t.forward((l/3)/3)
    t.left(300-a)
    t.forward((l/3)/3)
    t.left(a)
    t.forward((l/3)/3)
    t.left(300-a)
    t.forward((l/3)/3)
    t.left(a)
    t.forward((l/3)/3)
    t.left(300-a)
    t.forward((l/3)/3)
    t.left(a)
    t.forward((l/3)/3)
    t.left(a)
    
    
t.up()
t.goto(-300,0)
t.down()

nl=l/3
def draw(e):
    t.forward(nl/3**e)
    t.left(a)
    t.forward(nl/3**e)
    t.left(300-a)
    t.forward(nl/3**e)
    t.left(a)
    t.forward(nl/3**e)

for x in range(11):
    draw(1)
    t.left(a)
    draw(1)
    t.left(300-a)
    draw(1)
    t.left(a)
    

t.up()
t.goto(-300,-100)
t.down()

##смешная хрень)))
def new_draw_p():
    draw(2)
    t.left(a)
    draw(2)
    t.left(300-a)
    draw(2)
    t.left(a)
    draw(2)
    t.left(a)
    
for x in range(2):
    new_draw_p()
    t.left(a)
    new_draw_p()
    t.left(300-a)
    new_draw_p()
    t.left(a)

t.up()
t.goto(-300,-200)
t.down()

def new_draw():
    draw(2)
    t.left(a)
    draw(2)
    t.left(300-a)
    draw(2)
    t.left(a)
    draw(2)
   
    
for x in range(11):
    new_draw()
    t.left(a)
    new_draw()
    t.left(300-a)
    new_draw()
    t.left(a)    
