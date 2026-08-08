import turtle
wn = turtle.Screen()
bob = turtle.Turtle()
bob.shape("blank")
# bob.hideturtle()  # shape("blank") makes the turtle, not the pen, invisible same as hideturtle()
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

bob.right(135)
bob.forward(35.36)
bob.right(90)
bob.forward(35.36)
bob.right(135)

wn.exitonclick()

# medium height roof means the vertex angle is 90 degrees and each base angle is 45 deg.