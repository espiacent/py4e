def computepay(h, r):
    if h > 40:
        pay = ((h - 40) * (r * 0.5)) + (h * r)
        extra = h / r
        return pay
    else:
        pay = h * r
        return pay


inp1 = input('Enter Hours:')
inp2 = input('Enter Rate:')

try:
    hrs = float(inp1)
    mon = float(inp2)
except:
    print('Invalid input.')
    quit()

p = computepay(hrs, mon)
print("Pay", p)
