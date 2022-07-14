import time
for n in [10, 9, 8, 7, 5, 4, 3, 2, 1, 0]:
    print(n, end='')
    print('\a')
    time.sleep(1)
print('Liftoff!', end='')
print('\a')
