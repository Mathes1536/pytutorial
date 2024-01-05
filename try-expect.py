#try expect block execute try if any error use catch
try:
    name = 'test'
    age = int(name) #cannot convert string to int
    print(age)

except:
    print(name)



# try expect block to validate age 
data = input('Enter your age ')
try:
    age = int(data)
    if(age<18):
        print('You are not eligible')
    else:
        print('You are eligible')

except:
    print('Invalid input')