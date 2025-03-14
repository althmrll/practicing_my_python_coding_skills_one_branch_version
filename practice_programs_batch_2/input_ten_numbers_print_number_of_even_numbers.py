global counter
global even
 
#ask user to input ten numbers
counter=0
even= 0
 
while counter!=10:
    print("\ncounter:", counter)
    input_number= int(input("Enter number:"))
    counter= counter+1
 
#determine which are odd and even
    if input_number%2==0:
        even= even+1
 
#print the number of even numbers
print ("\nthere are", even, "even numbers in the numbers you inputted")