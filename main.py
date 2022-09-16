import turtle
from turtle import Turtle, Screen
import drawing

screen = Screen()
screen.bgcolor("#000000")

# Base Turtle Description
franklin = Turtle()
franklin.shape("turtle")
franklin.color("Dark Sea Green")
franklin.shapesize(1.5, 1.5)
franklin.pensize(10)
turtle.colormode(255)

# Examples using the functions in drawing.py
drawing.shape_drawing_turnaround(franklin, 3, 10)
franklin.clear()
drawing.dashed_line(franklin, 50, 10)
franklin.clear()
drawing.random_walk(franklin, 25)
franklin.clear()
drawing.spirograph(franklin, 15)

screen.exitonclick()
