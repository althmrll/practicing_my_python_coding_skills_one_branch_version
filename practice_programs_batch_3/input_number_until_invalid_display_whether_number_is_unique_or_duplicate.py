inputted_number= []
 
#input number(use while loop)
while True: #determine whether input is invalid
    try:
        number= int(input("Enter number:"))
        inputted_number.append(number)
        filtered_list=set(inputted_number)
 
        if len(inputted_number)==len(filtered_list): #determines whether the number is unique or a duplicate
            print("Unique") #displays when the number is unique
        else:
            print("Duplicate") #displays when the number is a duplicate
 
    except ValueError:
        print("!!INVALID INPUT!!")
        break