import turtle
wn = turtle.Screen()

def close_window():
    wn.bye()

wn.listen()
wn.onkey(close_window, "Escape")
alex = turtle.Turtle()
alex.forward(150)
alex.left(90)
alex.forward(75)
alex.salary = 50000
print(alex.salary)
alex.left(90)
alex.forward(150)
alex.left(90)
alex.forward(75)
wn.mainloop()