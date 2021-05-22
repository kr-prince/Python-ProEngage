import turtle  
import time

# Creating turtle screen  
t = turtle.Turtle() 

turtle.bgcolor("blue")
turtle.title("Turtle Learning")

time.sleep(1)
# changes the size and shape of the turtle
t.shapesize(stretch_wid=5, stretch_len=5, outline=12)

time.sleep(1)
# changes the thickness of the pen
t.pensize(5)
t.fd(100)
t.fillcolor("red")
t.pencolor("green")
# Same as t.color("green", "red")
# first is pen color, second is the fill color

t.fd(100)

t.shape("turtle")
time.sleep(1)
t.shape("arrow")
time.sleep(1)
t.shape("circle")
time.sleep(1)

turtle.exitonclick()