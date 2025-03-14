global counter
inputted_number=[]
counter = 0

#Ask user to input ten numbers
while counter!=10:
    number_input=int(input("Enter number:"))
    counter=counter+1
    
    if len(current_numbers)!=len(inputted_number): #Determine whether user inputted a number more than one time
        inputted_number.remove(number_input)
    else:
        inputted_number.append(number_input)
        current_numbers=set(inputted_number)
 
print(inputted_number) #print numbers without duplicate