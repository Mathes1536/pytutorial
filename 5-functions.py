def age_eligibilty(age):
#function always starts with 'def - basically functions we define'
    if(age<18):
            op = 'Not Eligible for Dlicense & VoterID'
    elif(age>=18):
            op = 'Eligible for Dlicense & VoterID'

    return op;





# Function to find max and min of numbers or characters.
def mxmnfunction(type,data):
      if(type=='text'):
            print('Maximmum  of the text in the input')
            op = (max(data))
            return op;
      elif(type=='number'):
            print('Maximum occured number in the input')
            op = (max(data))

      return op;
      


getinp = input(' Eligible calulator or Maximmum calulator \n Press 1 for Eligblity calc \n Press 2 for Maximum calculator')
getinp = int(getinp)

if(getinp==1):
    try:
        print('Enter your age')
        age = int(input())
        print(age_eligibilty(age))
    except:
        print('Please enter age in numbers')

elif(getinp==2):
      print('Enter the type of data you want to find max and min \n "text" for string \n "number" for number comparision')
      type = input()
      data = input()
      print(mxmnfunction(type,data))