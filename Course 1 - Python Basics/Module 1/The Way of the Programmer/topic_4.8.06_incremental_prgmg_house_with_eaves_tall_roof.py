import turtle
wn = turtle.Screen()
bob = turtle.Turtle()
bob.shape("blank")
# bob.hideturtle()  # shape("blank") makes the turtle, not the pen, invisible same as hideturtle()
bob.pensize(3)
# bob.width(3)  # pensize does same thing as width
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

bob.forward(10)
bob.right(120)
bob.forward(70)
bob.right(120)
bob.forward(70)
bob.right(120)
bob.forward(10)

wn.exitonclick()

# short roof means the vertex angle is 120 degrees and each base angle is 30 deg.