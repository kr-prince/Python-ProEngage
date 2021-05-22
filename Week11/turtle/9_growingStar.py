import turtle

sc = turtle.Screen()
sc.setup(600, 600)
spiral = turtle.Turtle()
spiral.speed(10)
sc.bgcolor("black")

col=["yellow","blue","white","green"]

for i in range(40):
	spiral.forward(i*10)
	spiral.right(144)
	spiral.color(col[i%4])

sc.exitonclick()
