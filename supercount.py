print('Enter number. For exit enter "done".')
count = 0
total = 0
while True:
    line = input('Input number:')
    if line == 'done':
        break
    try:
        line = float(line)
    except:
        print('Not a number.')
        continue
    else:
        count = count + 1
        if count > 1:
            total = total + line
        else:
            total = line
        print(line)
        continue
print('Done!')
print('Count:', count)
print('Total:', total)
if count > 1:
    print('Average:', total / count)
