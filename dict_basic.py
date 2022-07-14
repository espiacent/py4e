# print all values and keys of a dictionary
counts = {'elefant': 30, 'penis': 30, 'diamond': 10, 'something': 31020}
for key in counts:
    print(key, counts[key])

# count how many times words come up in a text
wordlist = dict()
line = input('Enter text:')
words = line.split()

for word in words:
    # key idiom for this:
    wordlist[word] = wordlist.get(word, 0) + 1
print(wordlist)

# take out key and value in one iteration using two variables
for a, b in wordlist.items():
    print(a, b)
