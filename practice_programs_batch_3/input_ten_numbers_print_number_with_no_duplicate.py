inputted_numbers=[]
counter= 0

#Ask user to input ten numbers
while counter!=10:
    print("\n numbers inputted:", counter)
    number_input= int(input("Enter number:"))
    counter= counter+1
    inputted_numbers.append(number_input)
 
#Determine whether user inputted a number more than one time
    if inputted_numbers.count(number_input)>1:
        while inputted_numbers.count(number_input)>=1:
            inputted_numbers.remove(number_input)
    else:
        continue
 
#print numbers without duplicate
print(inputted_numbers)