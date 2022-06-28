fname = input('Enter file name:')
if len(fname) < 1:
    fname = "mbox-short.txt"
try:
    fhand = open(fname, 'r')
except:
    print('Document not found.')
    raise SystemExit

days = {}
line2 = []
for line in fhand:
    if not line.startswith('From') or line.startswith('From:') or line.find('@') == -1: continue
    line = line.strip().split()
    mail = line[1]
    line2.append(mail)

for word in line2:
        days[word] = days.get(word, 0) + 1

#get value and key
amount = max(days.values())
name = max(days, key=days.get) #???
print(name, amount)