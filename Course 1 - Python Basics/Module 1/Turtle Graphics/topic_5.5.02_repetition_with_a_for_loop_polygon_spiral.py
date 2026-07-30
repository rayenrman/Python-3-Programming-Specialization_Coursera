import turtle
wn = turtle.Screen()

elan = turtle.Turtle()
elan.speed(5)

distance = 50
angle = 90
for _ in range(20):
    elan.forward(distance)
    elan.right(angle)
    distance += 10
    angle -= 3
wn.exitonclick()