global middle_number
 
#ask user to input numbers
lower_number= int(input("Enter lower limit:"))
higher_number= int(input("Enter higher limit:"))
 
#continue adding one until it reaches just below the higher number befre stopping
for i in range (lower_number, higher_number):
    middle_number=i+1
    print(middle_number) #print the numbers between them