# Making smart loops
# largest number in a list

my_list = [1, 2, 3, 4, 55, 6, 7, 8, 9, 10]

#something at begining
largest_num = my_list[0]

for number in my_list:
    if number > largest_num:
        largest_num = number

#something at end        
print('Largest number in my_list', largest_num)




# get count how many times the loop excuted & Average of the list
my_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#something at begining
largest_num = my_num[0]
count = 0
sum=0

for number in my_num:
    count=count+1
    sum=sum+number
    print(count,'.',sum)
    if number > largest_num:
        largest_num = number

print('Times the loop iterated ',count)
print('Total sum of the loop', sum)
print('Average sum of the loop ',sum/count)





#find the smallest in the list
# None is a datatype 

smallest_num = None
mysmall_list = [1, 2, 3, 4, 55, 6, 7, 8, 9, 10]

for number in mysmall_list:
    if smallest_num is None:
        smallest_num = number
    if number < smallest_num:
        smallest_num = number
    
print('Smallest number in my_list', smallest_num)