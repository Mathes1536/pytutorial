#Print statement
print('hello');

#No DataType Defined
width = 15
height = 12.0
print(height/3)

#Get input from the runtime explorer
user_name = input('Enter your Name ')
print('Welcome ',user_name)


#Compute gross pay by asking the hours and rate
hours = input('Enter Hours ')
rate = input('Enter Rate ')
pay = float(hours)*float(rate)
print('Calculated Pay ',pay)
#type conversion 
round_pay = int(pay)
print("Rounded Amount",round_pay)


# Operator Precedence   
#1.Parenthesis
#2. Power
#3. Multiplication
#4. Division
#5. Addition
#6. Subtraction
#7. LefttoRight

x = 1 + 2 ** 3 / 4 * 5
print('Order of Precedence',x)

#type - Print the type of variable
print(type(pay))


#US elevator floor conversion
get_floor = input('Enter the floor ')
floor_output = int(get_floor)+1
print('Your Floor',floor_output)