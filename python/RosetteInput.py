
import turtle

t = turtle.Pen()
t.shape('turtle')
t.speed(0)
turtle.bgcolor('black')

colors=['red', 'cyan', 'magenta', 'seashell', 'orange', 'green',
        'white', 'yellow', 'blue', 'pink', 'gray', 'purple', 'brown',
        'beige', 'royal blue', 'lime green', 'deep pink',
        'deep sky blue', 'lavender', 'orchid', 'thistle1', 'plum1',
        'firebrick1', 'DarkOrchid4', 'goldenrod1', 'IndianRed1']

##print(len(colors))

number = int(turtle.numinput("Number of circles",
                         "Give the number of circles", 4, 1))

for x in range(number):
    t.pencolor(colors[x%len(colors)])
    for y in range(100, 50, -10):
        t.circle(y)
        print(y)
    t.left(360/number)

  
