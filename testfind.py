try:
    handle = open('test.txt', 'r')
except:
    quit()

for line in handle:
    if line.find('9') == -1: continue
    startpos = line.find(':')
    num = line[startpos+1:]
    print(repr(line))
    
    
    #optional: num = num.strip()
    print(num)
    
    
    str = 'X-DSPAM-Confidence:    0.8475'
    startpos = str.find(':')
    num = str[startpos+1:]
    #optional: num = num.strip()
    num = float(num)
    print(num)