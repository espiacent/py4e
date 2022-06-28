# get input of hours and rate per hour; convert input to float
inp1 = input('How many hours?')
inp2 = input ('How much money?')
try:
    hours = float(inp1)
    rate = float(inp2)
except:
    print ('Invalid input.')
    quit()
def calcpay(value1, value2):
            rest = value1 - 40
            extra = rest * (value2 * 1.5)
            pay = (value1 - rest) * value2 + extra
            float(pay)
            print('The payment is:', pay)
# Check of input of hours is 40 or more than 40;
# if this is the case, calculate hours above 40
# and multiply by 1.5 and add to hours
if hours >= 40 :
        calcpay(hours, rate)
# if entered hours is less than 40, leave out the added extra    
else :
        pay = float(hours) * float(rate)
        pay = round(pay, 2)
        print('The payment is:', pay)
