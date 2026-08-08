import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
# tess.shape("circle")
# tess.shape("turtle")

# dist = 65
dist = 50
tess.up()
# for i in range(60):
for i in range(40):
    tess.stamp()
    tess.forward(dist)
    tess.left(28)
    dist -= 1

print('dist =', dist)
# tess.speed(1)
# tess.shape("classic")
# tess.shape("arrow")
# tess.shape("triangle")
# tess.color("magenta")
# tess.forward(150)
wn.exitonclick()

'''
This program is part of the ungraded app 5.6. A Few More turtle Methods and Observations.

All except one of the shapes you see on the screen here are footprints created by stamp. 
But the program still only has one turtle instance — can you figure out which one is the real tess? 
(Hint: if you’re not sure, write a new line of code after the for loop to change tess’ color, 
or to put her pen down and draw a line, or to change her shape, etc.)

Answer: The last turtle show on screen.
'''