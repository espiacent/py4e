inp = input('Enter a Score between 0.0 and 1.0:')
try:
    grade = float(inp)
except:
    print('Invalid input.')
    quit()
if grade >= 1.1:
    print('Entered value to high.')
    quit()
if grade < 0.0:
    print('Entered value to low.')
    quit()
elif grade >= 0.9:
    print('A')
elif grade >= 0.8:
    print('B')
elif grade >= 0.7:
    print('C')
elif grade >= 0.6:
    print('D')
elif grade < 0.6:
    print('F')
