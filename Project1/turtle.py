import turtle
import random

screen = turtle.Screen()
'''image1 = "C:\\turtle.gif"
image2 = "C:\\rabbit.gif"
screen.addshape(image1)
screen.addshape(image2)
'''
t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.color("pink")
t1.shape("turtle")
t1.shapesize(5)
t1.pensize(5)
t1.penup()
t1.goto(-300, 0)

t2.color("blue")
t2.shape("turtle")
t2.shapesize(5)
t2.pensize(5)
t2.penup()
t2.goto(-300, -200)

t1.pendown()
t2.pendown()
t1.speed(1)
t2.speed(1)

for i in range(100):
    d1 = random.randint(1, 60)
    t1.forward(d1)
    d2 = random.randint(1, 60)
    t2.forward(d2)
