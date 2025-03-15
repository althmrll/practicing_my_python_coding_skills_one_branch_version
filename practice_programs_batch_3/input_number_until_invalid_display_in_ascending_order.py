inputted_number=[]
 
#input number(use while loop)
while True: #determines whether input is invalid
    try:
        number=int(input("Enter number:"))
        inputted_number.append(number)
     
    except ValueError:
        arranged_list= inputted_number.sort()
        print(arranged_list) #sort all inputted numbers in ascending order
        break