inputted_number=[]

#input ten numbers
while True: #determines whether input is invalid
    try:
        number=int(input("Enter number:"))
        inputted_number.append(number)#adds each input on the list
        inputted_number.count #determines whether a value has repeated
     
    except ValueError:
        print(inputted_number)
        break

#print all inputted numbers except duplicates