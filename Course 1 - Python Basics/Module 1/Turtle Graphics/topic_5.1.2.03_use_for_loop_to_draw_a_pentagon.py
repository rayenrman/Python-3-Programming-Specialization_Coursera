import turtle
wn = turtle.Screen()

def close_window():
    wn.bye()

wn.listen()
wn.onkey(close_window, "Escape")
alex = turtle.Turtle()
for i in range(5):
    alex.forward(150)
    alex.left(72)
wn.mainloop()