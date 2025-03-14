global counter
inputted_number=[]
#Ask user to input ten numbers
while counter!=10:
    number_input=int(input("Enter number:"))
    counter=counter+1
    inputted_number.append(number_input)
#Determine whether user inputted a number more than one time
#print numbers without duplicate