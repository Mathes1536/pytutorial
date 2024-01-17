#open() - This method returns the handle of the file
#open(filename,mode)
#handle - is the bridge to get the file read write

handle = open('sample-files.txt','r')
print(handle)

#file handle as sequence
xfile = open('sample-files.txt')
for cheese in xfile:
    print(cheese)


#count number of lines in file
fhand = open('sample-files.txt')
count =0
for iteration in fhand:
    count+=1
print('Total lines in the file ',count)


#reading the *Whole file*
open_file = open('sample-files.txt')
inp = open_file.read()
print("Length of the file using read method",len(inp))


#searching through file
gethand = open('sample-files.txt')
for line in gethand:
    if line.startswith('From:'):
        print(line)

# searching through file effectievely 
gethand = open('sample-files.txt')
for line in gethand:
    if not line.startswith('From:'):
        continue
    line = line.rstrip()
    print(line)