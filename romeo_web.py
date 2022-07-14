# parse through txt file, find unique words, create sorted list of them

# get file name as input
import string
import urllib.request
import urllib.error
import urllib.parse

try:
    fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

except:
    print('File doesn\'t exist.')
    raise SystemExit()

# setting variables
unique = []
index = 0

# turn lines of file into lists
for line in fhand:
    list = line.decode().strip().split()
    # safety is line of file has nothing in it
    if len(list) == 0:
        continue
    # parse through all items in the made lists
    for words in list:
        words2 = words.lower()
        # get first item into new list
        if index == 0:
            unique.append(words2)
            index = index + 1
        # if item is not already in list, add item
        else:
            if words not in unique:
                unique.append(words2)

# finish program; sort list, print
unique.sort()
print(*unique, sep='\n')
