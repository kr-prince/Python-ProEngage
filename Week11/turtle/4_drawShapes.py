import turtle  
import time

# Creating turtle screen  
t = turtle.Turtle()  
 
# Draw a Rectangle
time.sleep(1)
t.fd(150)
time.sleep(1)
t.rt(90)
time.sleep(1)
t.fd(100)
time.sleep(1)
t.rt(90)
time.sleep(1)
t.fd(150)
time.sleep(1)
t.rt(90)
time.sleep(1)
t.fd(100)
time.sleep(1)


# Draw a preset shape
# t.circle(radius=100, extent=360, steps=50)
t.circle(radius=100)

turtle.mainloop()
