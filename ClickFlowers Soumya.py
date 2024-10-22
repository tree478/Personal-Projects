#ClickFlowers.py
import random
import turtle

turtle.bgcolor('black')
colors=['red', 'orange', 'yellow', 'green', 'blue', 'purple']

def draw_flower(x,y):
    t = turtle.Pen()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.setpos(x,y)
    t.pendown()
    c1 = random.choice(colors)
    c2 = random.choice(colors)
    t.width(random.randint(1,5))
    radius = random.randint(6,24)
    t.pencolor(c1)
    for m in range(radius//2):
        t.circle(radius)
        t.left(360/radius*2)
    t.pencolor(c2)
    for m in range(radius//2):
        t.circle(radius/3)
        t.left(360/radius*2)

turtle.onscreenclick(draw_flower)




