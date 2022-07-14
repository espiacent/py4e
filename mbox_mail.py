# Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.


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
    if not line.startswith('From') or line.startswith('From:') or line.find('@') == -1:
        continue
    line = line.strip().split()
    mail = line[1]
    line2.append(mail)

for word in line2:
    days[word] = days.get(word, 0) + 1

for a, b in days.items():
    print(a, b)

# print(days)
