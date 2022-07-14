str = 'X-DSPAM-Confidence:    0.8475'
startpos = str.find(':')
num = str[startpos+1:]
#optional: num = num.strip()
num = float(num)
print(num)
