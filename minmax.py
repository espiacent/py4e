print('Find largest and smallest number. Enter numbers. To end and calculate enter "done".')
max = 0
min = 0
count = 0
while True:
    line = input('Input number:')
    if line == 'done':
        break
    try:
        line = float(line)
    except:
        print('Invalid input. Enter number.')
        continue
    else:
        count = count + 1
        if count > 1:
            if line > max:
                max = line
            elif line < min:
                min = line
        else:
            max = line
            min = line
        continue
print('Largest entered number was:', max)
print('Smallest entered number was:', min)
print('Glad I could help.')
