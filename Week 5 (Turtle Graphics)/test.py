# import turtle
import turtle

# defining colors
colors = ['red', 'yellow', 'green', 'purple', 'blue', 'orange']

# setup turtle pen
t= turtle.Pen()

# changes the speed of the turtle
t.speed(50)

# changes the background color
turtle.bgcolor("black")

# make spiral_web
for x in range(100):
    t.pencolor(colors[x%6]) # setting color
    t.width(x/100 + 1) # setting width
    t.forward(x) # moving forward
    t.left(59) # moving left

t.penup()
t.goto(-20,200)
t.pendown()
t.left(180)
t.forward(30)
turtle.done()
t.speed(50)

turtle.bgcolor("black") # changes the background color

# make spiral_web
for x in range(600):
    t.pencolor(colors[x%6]) # setting color
    t.width(x/100 + 1) # setting width
    t.forward(x) # moving forward
    t.left(59) # moving left

turtle.done()
