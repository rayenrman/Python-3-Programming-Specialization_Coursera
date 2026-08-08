# This program is in Module 2, Part 1 - Lists and Strings, item 11 video, Length of Sequences
# It displays the middle character(s) of a fruit name that the user entered. 

fruit = input("Enter the name of a fruit: ").strip()
print(fruit, 'has', len(fruit), 'characters')
if len(fruit) % 2 == 1:  # length is an odd number
    midchar = fruit[len(fruit)//2]
    print("The middle character of", fruit, "is", midchar)
else:   # length is an even number
    midchar = fruit[(len(fruit)//2) - 1] + fruit[len(fruit)//2]
#    midchar = fruit[((len(fruit)//2) - 1) : ((len(fruit)//2) + 1)]
    print("The middle characters of", fruit, "are", midchar)
