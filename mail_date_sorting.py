'''
Exercise 2: This program counts the distribution of the hour of the day for each
of the messages. You can pull the hour from the “From” line by finding the time
string and then splitting that string into parts using the colon character. Once
you have accumulated the counts for each hour, print out the counts, one per line, 
sorted by hour as shown below.
'''

fname = input('Enter file name:')

if len(fname) < 1:
    fname = 'mbox-short.txt'

try:
    fhand = open(fname, 'r')
except:
    print('Document not found.')
    raise SystemExit

h_list = []
h_list_dict = {}
final_list = []

for line in fhand:
    if not line.startswith('From') or line.startswith('From:') or line.find('@') == -1:
        continue
    line = line.strip().split()
    date = line[5]
    hours = date[0:2]
    h_list.append(hours)

for hour in h_list:
    h_list_dict[hour] = h_list_dict.get(hour, 0) + 1

    # alternative:
    # if hour not in h_list_dict:
    #h_list_dict[hour] = 1
    # else:
    #h_list_dict[hour] += 1

for k, v in list(h_list_dict.items()):
    final_list.append((k, v))

final_list.sort()

for k, v in final_list[:]:
    print(k, v)
