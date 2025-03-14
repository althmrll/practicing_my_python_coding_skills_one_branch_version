global counter
global odd
 
counter = 0
odd = 0
 
#Ask user ot input ten numbers
while number != 10:
    input_number = int(input("Enter number:"))
    counter = counter + 1
 
 #Determine whether the inputted number is odd
    if input_number % 2 == 1:
        odd = odd + 1

#Print how many are odd
print("There are", odd, "odd numbers in the ten numbers you inputted.")