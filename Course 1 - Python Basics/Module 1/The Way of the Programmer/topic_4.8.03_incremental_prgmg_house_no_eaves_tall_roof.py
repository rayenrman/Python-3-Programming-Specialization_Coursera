import turtle
wn = turtle.Screen()
bob = turtle.Turtle()
bob.hideturtle()
# bob.shape("blank")  # shape("blank") makes the turtle, not the pen, invisible same as hideturtle()
bob.width(2)
# bob.pensize(2)  # pensize does same thing as width

bob.right(90)
bob.forward(50)
bob.left(90)
bob.forward(50)
bob.left(90)
bob.forward(50)
bob.left(90)
bob.forward(50)

bob.right(120)
bob.forward(50)
bob.right(120)
bob.forward(50)
bob.right(120)

wn.exitonclick()

# short roof means the vertex angle is 120 degrees and each base angle is 30 deg.