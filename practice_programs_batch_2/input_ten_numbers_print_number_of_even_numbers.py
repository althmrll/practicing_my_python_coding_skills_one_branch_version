global counter
global even
 
#ask user to input ten numbers
while counter!=10:
    print("counter:", counter)
    input_number= int(input("Enter number:"))
    counter= counter+1
 
#determine which are odd and even
    if input_number%2==0:
        even= even+1
 
#print the number of even numbers
print ("there are", even, "even numbers in the numbers you inputted")