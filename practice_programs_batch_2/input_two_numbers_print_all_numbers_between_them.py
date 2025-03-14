global start
 
#ask user to input numbers
lower_number= int(input("Enter lower limit:"))
higher_number= int(input("Enter higher limit:"))
start=lower_number+1
 
#continue adding one until it reaches just below the higher number befre stopping
for i in range (start, higher_number):
    print(i) #print the numbers between them
    i=i+1