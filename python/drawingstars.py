#drawing stars with 3 arguments: size of turtle's step (spine of star), numbers of points and number of rounds, turtle goes to draw the star.
#in this variant angles are calculated iaw simple math formulas

print('Привет! Подскажите черепашке, какую звезду нарисовать')
print()

import sys

print('Введите желаемую длину лучей звезды')
size = int(sys.stdin.readline())
print('Введите желаемое количество лучей звезды')
points = int(sys.stdin.readline())
print('Введите любое число, которое меньше, чем количество лучей')
rounds = int(sys.stdin.readline())

import turtle
s = turtle.Pen()
turtle.bgcolor('cyan')
s.shape('turtle')

def draw_star(size, points, rounds):
    angle = 360/points
    if rounds % 2 == 0 and points % 2 == 0:
    	k = rounds
    else:
    	k = rounds + 1
    for x in range (0, points):
    	s.forward(size)
    	s.left(180-angle)
    	s.forward(size)
    	s.right(180-k*angle)

draw_star(size, points, rounds)
s.up()
s.backward(size*2)
