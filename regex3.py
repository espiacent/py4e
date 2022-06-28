import re

fname = input('Enter file name:')
if len(fname) < 1:
	fname = 'regex_sum_42.txt'
try:
	fhand = open(fname, 'r')

except:
	print('File doesn\'t exist.')
	raise SystemExit

t_lst = []
amount = 0
for line in fhand:
    line = line.strip()
    x = re.findall('[0-9]+', line)
    if len(x) == 0: 
    	continue
    elif len(x) > 0: 
    	t_lst.extend(x)
try:    	
	t_lst = list(map(int, t_lst))
	print(round(sum(t_lst)))
except:
	print('Something went wrong.')
	raise SystemExit