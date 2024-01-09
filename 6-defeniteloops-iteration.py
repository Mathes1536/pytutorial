#while loop in python with break statement
# while loop also called indefinite loop
print('===while loop in python with break statement====')
n=20
while n>10:
    print(n," is greater than 10")
    n=n-1
    if n==15:
        break


#while loop with continue statement
print('===while loop with continue statement====')
n='#test stirng'

while True:   
    print(n)
    if n[0]=='#':
        n=n[1:]
        continue
    quit()
   
   