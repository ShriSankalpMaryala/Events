import turtle
import random
screen = turtle.Screen()
list = ["yellow","red","blue","pink","green"]


def hello(x,y):
    color = random.choice(list)
    screen.bgcolor(color)

screen.onclick(hello)

turtle.done()