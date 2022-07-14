'''
Exercise 2: This program counts the distribution of the hour of the day 
for each of the messages. You can pull the hour from the “From” line by 
finding the time string and then splitting that string into parts using 
the colon character. Once you have accumulated the counts for each hour, 
print out the counts, one per line, sorted by hour as shown below.

'''

fname = input('Enter file name:')
if len(fname) < 1:
    fname = "mbox-short.txt"
try:
    fhand = open(fname, 'r')
except:
    print('Document not found.')
    raise SystemExit

addresses = {}
line2 = []
for line in fhand:
    if not line.startswith('From') or line.startswith('From:') or line.find('@') == -1:
        continue
    line = line.strip().split()
    mail = line[1]
    line2.append(mail)

for person in line2:
    if person not in addresses:
        addresses[person] = 1
    else:
        addresses[person] += 1

lst = []
for k, v in list(addresses.items()):
    lst.append((v, k))

lst.sort(reverse=True)

for k, v in lst[:1]:
    print(v, k)
