global input_number
global counter
global result

#Ask user to input ten numbers
#Find sum of ten numbers
counter = 0
result = 0
 
while counter != 10:
    print ("numbers inputted:", counter)
    input_number = int(input("Enter number:"))
    print("")
    result = result + input_number
    counter = counter + 1

#Print sum of the ten numbers
print("sum:", result)