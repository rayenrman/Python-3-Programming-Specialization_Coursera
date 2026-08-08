import turtle
wn = turtle.Screen()

timmy = turtle.Turtle()
timmy.speed(5)

distance = 1
angle = 1
for _ in range(40):
    timmy.forward(distance)
    timmy.right(angle)
    distance += 1.5
    angle += 1

wn.exitonclick()