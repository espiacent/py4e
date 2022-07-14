# get file name as input
fname = input('Enter file name:')

# safety if file doesn't exist
try:
    fhand = open(fname, 'r')

except:
    print('File doesn\'t exist.')
    raise SystemExit()

# setting variables
#unique = []
counter = 0

# turn lines of file into lists
for line in fhand:
    if not line.startswith('From'):
        continue
    elif line.startswith('From:'):
        continue
    counter = counter + 1
    line = line.strip().split()
    print(line[1])
    continue

print("There were", counter, "adresses in the file.")
