import turtle
wn = turtle.Screen()
bob = turtle.Turtle()
bob.hideturtle()
# bob.shape("blank")  # shape("blank") makes the turtle, not the pen, invisible same as hideturtle()
bob.width(3)
# bob.pensize(3)  # pensize does same thing as width
bob.color('green')
# bob.pencolor('green')  # pencolor is part of color ,i.e. color(pencolor, fillcolor, /)

bob.right(90)
bob.forward(50)
bob.left(90)
bob.forward(50)
bob.left(90)
bob.forward(50)
bob.left(90)
bob.forward(50)

bob.forward(15)
bob.right(135)
bob.forward(56.57)
bob.right(90)
bob.forward(56.57)
bob.right(135)
bob.forward(15)

wn.exitonclick()

# medium height roof means the vertex angle is 90 degrees and each base angle is 45 deg.