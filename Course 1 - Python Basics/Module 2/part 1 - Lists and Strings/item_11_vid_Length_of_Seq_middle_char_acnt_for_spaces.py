# This program is in Module 2, Part 1 - Lists and Strings, item 11 video, Length of Sequences
# It displays the middle character(s) of a fruit name that the user entered. 
# It accounts for blank spaces if it is a middle character.

fruit = input("Enter the name of a fruit: ").strip()
print(fruit, 'has', len(fruit), 'characters')
if len(fruit) % 2 == 1:  # length is an odd number
    midchar = fruit[len(fruit)//2]
    if midchar == ' ':
        midchar = "a blank space."
    print("The middle character of", fruit, "is", midchar)
else:   # length is an even number
    if fruit[(len(fruit)//2) - 1] == ' ':
        if fruit[len(fruit)//2] == ' ':
            midchar = 'both blank spaces'
        else:
            midchar = 'a blank space and ' + fruit[len(fruit)//2]
    elif fruit[len(fruit)//2] == ' ':
        midchar = fruit[(len(fruit)//2) - 1] + ' and a blank space.'
    else:
        midchar = fruit[(len(fruit)//2) - 1] + fruit[len(fruit)//2]
#        midchar = fruit[((len(fruit)//2) - 1) : ((len(fruit)//2) + 1)]  # same output as line above
    print("The middle characters of", fruit, "are", midchar)
