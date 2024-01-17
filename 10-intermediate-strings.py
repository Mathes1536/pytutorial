fruit = 'custard apple'

print(fruit[2:])
print(fruit[:5])


# use in as logical operator

print('n' in fruit) # false
print('c' in fruit) # true

# search character using if condition

if 'c' in fruit:
    print('c is present')

print(dir(fruit))

print(fruit.isdigit())
