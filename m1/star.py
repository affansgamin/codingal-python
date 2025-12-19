import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(500,350)
star = turtle.Turtle()

num_sides = 3 #variable
side_length = 60
angle = 360.0 / num_sides
#iterate loop for total number of side
for i in range(num_sides):
    star.forward(side_length)
    star.right(angle)
star.penup()
star.right(90)
star.forward(side_length*0.5)
star.left(90)
star.pendown()
for i in range(num_sides):
    star.forward(side_length)
    star.left(angle)
    
turtle.done()