import turtle
screen = turtle.Screen()

def close_window():
    screen.bye()

# Bind the function to a specific key (e.g., "Escape")
screen.listen()
screen.onkey(close_window, "Escape")
# Alternative: Bind to any key by omitting the second argument
# screen.onkey(close_window, "") 

alex = turtle.Turtle()
number_of_sides = 6
length_of_each_side_in_pixels = 70 * 1
# At 1080p on a 24-inch computer monitor, one inch = 92 to 93 pixels ≈ 90 pixels (92 ppi)
# At 1080p on a 27-inch computer monitor, one inch = 81 to 82 pixels ≈ 80 pixels (82 ppi)
# At 1080p on a 32-inch computer monitor, one inch = 69 pixels ≈ 70 pixels  (69 ppi)
sum_of_interior_angles = (number_of_sides - 2) * 180
interior_angle = sum_of_interior_angles / number_of_sides
exterior_angle = 180 - interior_angle
for i in range(number_of_sides):
    alex.forward(length_of_each_side_in_pixels)
    alex.left(exterior_angle)

# Keep the window running until an event occurs
# Must be placed at the very end of your script. 
# This prevents the Python execution process from immediately terminating, 
#    keeping the screen alive until an event is triggered.
screen.mainloop()