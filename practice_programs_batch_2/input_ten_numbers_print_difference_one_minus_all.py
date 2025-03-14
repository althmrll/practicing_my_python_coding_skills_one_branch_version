global counter
global total
 
#Ask user to input first number
counter= 0
print("inputted number:", counter)
first_number= int(input("Enter number:"))
counter= counter+1
 
#Ask user to input other 9 numbers
while counter!=10:
    print("inputted number:", counter)
    other_numbers=int(input("Enter another number:"))
    counter= counter+1 
    total=other_numbers+1 #Find total of the other 9 numbers
 
#subtract sum of the 9 numbers to the first number
difference= first_number-total
 
#Print their difference