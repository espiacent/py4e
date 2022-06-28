#New Revision: 39772

import re

fname = input('Enter file name:')
if len(fname) < 1:
	fname = 'mbox-short.txt'
try:
	fhand = open(fname, 'r')

except:
	print('File doesn\'t exist.')
	raise SystemExit

t_lst = []
amount = 0
for line in fhand:
    line = line.strip()
    x = re.findall('^N.*(\d{5})', line)
    if len(x) == 0: 
    	continue
    elif len(x) > 0: 
    	amount = amount + 1
    	t_lst.append(x[0])
    	
t_lst = list(map(int, t_lst))
print(round(sum(t_lst) / amount))