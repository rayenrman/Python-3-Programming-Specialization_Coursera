import turtle
wn = turtle.Screen()
jose = turtle.Turtle()
jose.shape("turtle")
jose.penup()
jose.speed(2)

for size in range(10):
    jose.forward(50)
    jose.stamp()
    jose.forward(-50)
    jose.right(36)

wn.exitonclick()

'''
This program is part of the ungraded app 5.6. A Few More turtle Methods and Observations.

The program should do all necessary set-up, create the turtle, 
set the shape to “turtle”, and pick up the pen. 
Then the turtle should repeat the following ten times: 
    go forward 50 pixels, 
    leave a copy of the turtle at the current position, 
    reverse for 50 pixels, 
    and then turn right 36 degrees. 
'''