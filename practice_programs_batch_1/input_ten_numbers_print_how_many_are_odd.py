global counter
global odd
 
counter = 0
odd = 0
 
#Ask user ot input ten numbers
while counter != 10:
    print ("numbers already inputted:", counter)
    input_number = int(input("Enter number:"))
    print ("")
 
 #Determine whether the inputted number is odd
    if input_number % 2 == 1:
        odd = odd + 1

#Print how many are odd
print("There are", odd, "odd numbers in the ten numbers you inputted.")