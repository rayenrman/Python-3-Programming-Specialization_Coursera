import turtle
wn = turtle.Screen()

def close_window():
    wn.bye()

wn.listen()
wn.onkey(close_window, "Escape")
alex = turtle.Turtle()
for i in range(4):
    odd_nbr_indicator = i % 2  # equal to 1 if odd nbr, 0 if even nbr
    alex.forward(75 * (2 - odd_nbr_indicator))
    alex.left(90)
wn.mainloop()