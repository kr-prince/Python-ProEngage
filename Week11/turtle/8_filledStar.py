import turtle

turtle.color("red", "yellow")

turtle.begin_fill()
while True:
	turtle.forward(200)
	turtle.left(170)
	print(turtle.pos())
	if abs(turtle.pos()) < 1:
		break

turtle.end_fill()
turtle.exitonclick()
