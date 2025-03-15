inputted_number=[]

#input ten numbers
while True: #determines whether input is invalid
    try:
        number=int(input("Enter number:"))
        inputted_number.append(number)#adds each input on the list
        filtered_list=set(inputted_number) #creates set that excludes all duplicates
     
    except ValueError:
        print(filtered_list) #prints the set
        break