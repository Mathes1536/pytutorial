# code to open a file and print(line by line) the character in uppercase

try:
    file = input('Enter a file name')
    file_handler = open(file)
except:
    print(' Please Enter a valid file name ', file)
    quit()



for iteration in file_handler:
    iteration = iteration.upper()
    print(iteration)

#print(file_handler.read())