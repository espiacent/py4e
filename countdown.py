import time
n = 10
while n > 0 :
        print(n, end='')
        print('\a')        
        time.sleep(1)
        n = n - 1
print(n, end='')
print('\a')    
time.sleep(1)
print('Liftoff!', end='')
print('\a')    
