##рисование линий Коха
import turtle
import random

t = turtle.Pen()
t.speed(0)
t.up()
t.goto(-300,200)
t.down()
turtle.bgcolor('black')
t.color('cyan')

##length of line - заданная длина линии
##l = 90

##с запросом длины линии у пользователя
##quest = input("Введи число - длину линии\n")
##l = int(quest)

##random length
l = random.randrange(30,300)
print('random length',l)

a = 60 ## angle

b = (a, 300-a, a) ##tuple of angles

def draw(e):
    for c in b:
        t.forward(l/3**e)
        t.left(c)
    t.forward(l/3**e)

## simple Koch's curve
for x in range(11):
    draw(1)

t.up()
t.goto(-300,100)
t.down()

## second variant of Koch's curve
def new_draw_1(e):
    for c in b:
        draw(e)
        t.left(c)
    draw(e)
    
for x in range(11):
    new_draw_1(2)

t.up()
t.goto(-300,0)
t.down()

## third variant of Koch's curve
def new_draw_2(e):
    for c in b:
        new_draw_1(e)
        t.left(c)
    
for x in range(11):
    new_draw_2(3)
   
