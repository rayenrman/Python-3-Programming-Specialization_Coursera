# Question no 4:
# A palindrome is a phrase that, if reversed, would read the exact same. 
# Write code that checks if p_phrase is a palindrome by reversing it and 
# then checking if the reversed version is equal to the original. 
# Assign the reversed version of p_phrase to the variable r_phrase so that we can check your work.
# given: p_phrase = "was it a car or a cat I saw"

p_phrase = "was it a car or a cat I saw"
space_and_punctuation_marks = [' ', '.', ',', '?', '!', "'", '"', ':', ';', '-']
for char in space_and_punctuation_marks:
#    p_phrase_condensed_lower = p_phrase.replace(char, '').lower()
    p_phrase_condensed = p_phrase.replace(char, '')
r_phrase = ''
# for letter in p_phrase_condensed_lower:
for letter in p_phrase_condensed:
    r_phrase = letter + r_phrase
# print(p_phrase_condensed_lower)S
print(p_phrase_condensed)
print(r_phrase)
if r_phrase.lower() == p_phrase.lower():
    print('It is a palindrome!')

# A logic error from lines 10 and 12 results in blank spaces not being removed.
# The solution is in another file.