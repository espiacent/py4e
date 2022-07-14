'''
Exercise 3: Write a program that reads a file and prints the letters in decreasing 
order of frequency. Your program should convert all the input to lower case and only 
count the letters a-z. Your program should not count spaces, digits, punctuation, or 
anything other than the letters a-z. Find text samples from several different languages 
and see how letter frequency varies between languages. Compare your results with the 
tables at https://wikipedia.org/wiki/Letter_frequencies.


'''

import string

fname = input('Enter file name:')
if len(fname) < 1:
    fname = 'romeo-full.txt'

try:
    fhand = open(fname, 'r')
except:
    print('File not found.')
    raise SystemExit

lst = []
for line in fhand:
    line = line.lower().strip()
    line2 = line.translate(str.maketrans('', '', string.punctuation))
    lst.append(line2)

lst2 = list(filter(None, lst))
str1 = ''.join(lst2)
lst2 = list(str1)
letters = {}
final_list = []

for letter in lst2:
    letters[letter] = letters.get(letter, 0) + 1

for k, v in list(letters.items()):
    final_list.append((k, v))

final_list.sort()

for k, v in final_list[2:]:
    print(k, v)
