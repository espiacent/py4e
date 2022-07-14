def computegrade(x):

    if x >= 0.9:
        grade = 'A'
    elif x >= 0.8:
        grade = 'B'
    elif x >= 0.7:
        grade = 'C'
    elif x >= 0.6:
        grade = 'D'
    elif x < 0.6:
        grade = 'F'
    return grade


inp = input('Enter a Score between 0.0 and 1.0:')

try:
    inp = float(inp)
except:
    print('Invalid input.')
    quit()

if inp >= 1.1:
    print('Entered value to high.')
    quit()
if inp < 0.0:
    print('Entered value to low.')
    quit()
else:
    score = computegrade(inp)
    print('The score is:', score)
