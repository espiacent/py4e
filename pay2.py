# get input of hours and rate per hour; convert input to float
inp1 = input('How many hours?')
inp2 = input('How much money?')
try:
    hours = float(inp1)
    rate = float(inp2)
except:
    print('Invalid input.')
    quit()
# Check of input of hours is 40 or more than 40;
# if this is the case, calculate hours above 40
# and multiply by 1.5 and add to hours
if hours >= 40:
    rest = hours - 40
    extra = rest * rate * 1.5
    pay = (hours - rest) * rate
    pay = pay + extra
    print('The payment is:', pay)
# if entered hours is less than 40, leave out the added extra
else:
    pay = float(hours) * float(rate)
    pay = round(pay, 2)
    print('The payment is:', pay)
