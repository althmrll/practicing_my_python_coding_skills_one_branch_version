inputted_number=[]

#input ten numbers
while True: #determines whether input is invalid
    try:
        number=int(input("Enter number:"))
        inputted_number.append(number)#adds input on the list
     
    except ValueError:
        break
#print all inputted numbers except duplicates