import turtle
wn = turtle.Screen()

def close_window():
    wn.bye()

wn.listen()
wn.onkey(close_window, "Escape")
alex = turtle.Turtle()
for i in range(2):
    alex.forward(150)
    alex.left(90)
    alex.forward(75)
    alex.left(90)
wn.mainloop()