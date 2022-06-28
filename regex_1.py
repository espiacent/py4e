import re

fname = input('Enter file name:')
regex = input('Enter RE:')

try:
	fhand = open(fname, 'r')

except:
	print('File doesn\'t exist.')
	raise SystemExit

amount = 0
for line in fhand:
    line = line.strip()
    x = re.findall(regex, line)
    if len(x) > 0: amount = amount + 1
print(amount)