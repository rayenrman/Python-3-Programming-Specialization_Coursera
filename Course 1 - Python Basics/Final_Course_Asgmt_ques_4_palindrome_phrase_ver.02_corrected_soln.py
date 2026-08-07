# Question no 4:
# A palindrome is a phrase that, if reversed, would read the exact same. 
# Write code that checks if p_phrase is a palindrome by reversing it and 
# then checking if the reversed version is equal to the original. 
# Assign the reversed version of p_phrase to the variable r_phrase so that we can check your work.
# given: p_phrase = "was it a car or a cat I saw"
# This version, ver.02, removes the blank spaces between words.

p_phrase = "was it a car or a cat I saw"
# p_phrase = "Cigar? Toss it in a can. It is so tragic."
# p_phrase = "Go hang a salami, I'm a lasagna hog."
# p_phrase = "Madam in Eden, I'm Adam."
# p_phrase = "Though the man—Ferdinand de Lesseps— first made a canal plan for Suez."
space_and_punctuation_marks = [' ', '.', ',', '?', '!', "'", '"', ':', ';', '-', '–', '—']
p_phrase_original = p_phrase
print('p_phrase_original :', p_phrase_original)
print('p_phrase(at start):', p_phrase)
for char in space_and_punctuation_marks:
    p_phrase = p_phrase.replace(char, '').lower()
#    p_phrase = p_phrase.lower().replace(char, '')  # also works since lower() and replace() can be in any order
r_phrase = ''
for letter in p_phrase:
    r_phrase = letter + r_phrase
print('p_phrase(at end)  :', p_phrase)
print('r_phrase          :', r_phrase)
if r_phrase == p_phrase:
    print('It is a palindrome!')
else:
    print('It is NOT a palindrome!')
