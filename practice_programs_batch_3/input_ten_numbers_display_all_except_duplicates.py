inputted_number=[]

#input ten numbers
while True: #determines whether input is invalid
    try:
        number=int(input("Enter number:"))
        inputted_number.append(number)#adds each input on the list
        inputted_number.count(number) #determines whether a value has repeated
 
        if inputted_number.count(number)>1:
            inputted_number.remove #print all inputted numbers except duplicates
     
    except ValueError:
        print(inputted_number)
        break