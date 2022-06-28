'''
Exercise 5: This program records the domain name (instead of the address) 
where the message was sent from instead of who the mail came from (i.e., the whole email 
address). At the end of the program, print out the contents of your dictionary.
'''

#mbox-short.txt
#{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7 ...}

import time

fname = input('Enter file name:')
if len(fname) < 1:
    fname = "mbox-short.txt"
try:
    fhand = open(fname, 'r')
except:
    print('Document not found.')
    raise SystemExit

domains = {}
line2 = []
for line in fhand:
    if not line.startswith('From') or line.startswith('From:') or line.find('@') == -1: continue
    line = line.strip().split()
    mail = line[1]
    address = mail.split('@')
    domain = address[1]
    line2.append(domain)

for word in line2:
        domains[word] = domains.get(word, 0) + 1 #comment below
        '''
        basically adds items from list with domains and gets value of it, if not 
        existing alternative value is 0, then 1 is added. ends in dictionary with 
        all items of list as keys and values of times the item was found in list.
        '''

value = list(domains.values())
key = list(domains.keys())
print(key[value.index(max(value))], max(domains.values()))#comment below

#(key[value.index(max(value))] --> the key is the list of keys, so we want the key at the position of the highest value. highest value is by indexing the values with value highest value.
#of values the highest value is the max value already.