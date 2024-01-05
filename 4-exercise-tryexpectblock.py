#Rewrite pay computation to give employee 1.5 times the hourly rate.

print('== Numeric Employee Pay Calculator ===')
hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
pay = float(hours)* float (rate) * 1.5
print('The Actual pay ','$', pay,)


# the above program with try expect catch

print('== Employee Pay Calculator ===')

try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
    pay = (hours*rate) * 1.5
    print('The Actual pay ','$', pay,)
except:
    print('Error, please enter numeric input')
    quit()
print('out from the try catch block')