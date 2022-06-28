#Exercise 1: Write a while loop that starts at the last character in the string and works #its way backwards to the first character in the string, printing each letter on a #separate line, except backwards.

index = -1
word = 'elefant'
length = len(word) * -1

while index >= length:
    letter = word[index]
    print(letter)
    index = index - 1