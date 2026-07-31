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
bob.right(150)
bob.forward(46.2)
bob.right(60)
bob.forward(46.2)
bob.right(150)
bob.forward(15)

wn.exitonclick()

# short roof means the vertex angle is 120 degrees and each base angle is 30 deg.