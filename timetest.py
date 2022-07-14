# basis
import time
from time import ctime

# get time
sec = time.time()
print(sec)
curr = time.ctime(sec)
print(curr)

# get time shorter
curr = time.ctime(time.time())
print(curr)

# get time even shorter
print(time.ctime(time.time()))

# shortest
print(ctime())

# note:
# time.time gives float
# time.ctime gives string
