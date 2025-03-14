global middle_number
 
#ask user to input numbers
lower_number= int(input("Enter lower limit:"))
higher_number= int(input("Enter higher limit:"))
 
#Add one to lower number of the two(lowernumber+1)
middle_number= lower_number+1
 
#continue adding one until it reaches just below the higher number befre stopping
while lower_number<higher_number:
    print(middle_number) #print the numbers between them
    middle_number=middle_number+1