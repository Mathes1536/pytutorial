#open file dynamically with input from user


try:
    file = input('Enter the file name')
    file_handler = open(file)
except:
    print('Please Enter a valid file name: ',file)
    quit()

count = 0
for item in file_handler:
    if not item.startswith('From:'):
        continue
    count = count+1
print(' Number of mail address available in the file: ',file,' is ',count)
    