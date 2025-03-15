inputted_number=[]
 
#input number(use while loop)
while True: #determines whether input is invalid
    try:
        number=int(input("Enter number:"))
        inputted_number.append(number)
     
    except ValueError:
        print(sort(inputted_number)) #sort all inputted numbers in ascending order
        break