import turtle

print('The valid color names are at https://www.w3schools.com/colors/colors_names.asp')
background_color = input('Enter color of background: ')
pen_color = input('Enter color of the pen: ')
print('pensize = 1 (Default): Thin, sharp, and standard for regular line drawings and detailed shapes.')
print('pensize = 3 to 5: Medium thickness, commonly used to make shapes or text slightly more visible on screen.')
print('pensize = 8 to 10: Bold and thick, useful for highlighting borders or filling visual structures with heavy lines.')
pen_width_str = input('Enter size or width of the pen: ')
pen_width = int(pen_width_str)

wn = turtle.Screen()
wn.bgcolor(background_color)        # set the window background color

tess = turtle.Turtle()
tess.color(pen_color)              # make tess blue
tess.pensize(pen_width)                 # set the width of her pen

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.exitonclick()                # wait for a user click on the canvas

'''
An object can have various methods — things it can do — and it can also have attributes — (sometimes called properties). 
For example, each turtle has a color attribute. The method invocation alex.color("red") will make alex red and the line that it draws will be red too.

The color of the turtle, the width of its pen(tail), the position of the turtle within the window, 
which way it is facing, and so on are all part of its current state. Similarly, the window object has a background color which is part of its state.
'''