import turtle
wn = turtle.Screen()

elan = turtle.Turtle()
elan.speed(3)

distance = 50
for _ in range(10):
    elan.forward(distance)
    elan.right(90)
    distance += 10
wn.exitonclick()