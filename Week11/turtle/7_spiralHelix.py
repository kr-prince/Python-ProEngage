import time
import turtle

loadWindow = turtle.Screen()
# This is used to control the speed of writing
turtle.speed(10)
 
for i in range(30):
	turtle.circle(5*i)
	turtle.circle(-5*i)
	turtle.left(i)
 
turtle.exitonclick()