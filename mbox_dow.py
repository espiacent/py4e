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
    if not line.startswith('From') or line.startswith('From:'):
        continue
    line = line.strip().split()
    date = line[2]
    line2.append(date)

for word in line2:
    days[word] = days.get(word, 0) + 1

for a, b in days.items():
    print(a, b)

# print(days)
