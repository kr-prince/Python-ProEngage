import turtle  
import time

# Creating turtle screen  
t = turtle.Turtle()  
 
# Returns turtle current heading - direction in angle
time.sleep(2)
print(t.heading())

# Turtle can move in four directions - Forward, Backward, 
# Left, Right are to change directions
# Move turtle in opposite direction  
t.right(90)

time.sleep(2)
print(t.heading())
t.forward(100)

time.sleep(2)
print(t.heading())
t.left(90)

time.sleep(2)
print(t.heading())
t.backward(100)
  

time.sleep(2)
t.goto(200,200)
time.sleep(2)
t.home()    # Home is the initial position of the tutle(0,0)


# To stop the screen to display  
turtle.mainloop()  