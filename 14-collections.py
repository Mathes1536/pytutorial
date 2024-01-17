# collections is like suit cases
# this can hold multiple data in a variable using list, dictionary
# strings are immutable {cannot change the data}
# list are mutable {can change the contents}

friends = ['Abishek', 'Deepoli', 'Jai']
backpack = ['Dress', 'Shoe', 'Perfume']

backpack[2] ='Bella vita perfume'


#range function
print(len(backpack))

#loop in the list
for i in range(len(backpack)):
    list = backpack[i]
    print('Content in the backpack ',list)