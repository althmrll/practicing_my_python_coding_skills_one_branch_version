global counter
inputted_number=[]

#Ask user to input ten numbers
while counter!=10:
    number_input=int(input("Enter number:"))
    counter=counter+1
    inputted_number.append(number_input)
    unique_numbers=set(inputted_number)
    if len(set)!=len(inputted_number): #Determine whether user inputted a number more than one time
        inputted_number.remove()
 
print(inputted_number) #print numbers without duplicate