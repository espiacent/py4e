def count():
    count = 0
    for letter in inp1:
        if letter == inp2:
            count = count + 1
    print(count)


inp1 = input('Enter word:')
inp2 = input('Enter letter:')

count()
