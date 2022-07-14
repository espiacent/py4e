try:
    handle = open('mbox-short.txt')
except:
    quit()

text = handle.read()
bold = text.upper()

print(bold)
