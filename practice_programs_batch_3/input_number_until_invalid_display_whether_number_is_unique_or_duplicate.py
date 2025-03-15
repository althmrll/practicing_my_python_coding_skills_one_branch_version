inputted_number= []
 
#input number(use while loop)
while True: #determine whether input is invalid
    try:
        number= int(input("Enter number:"))
        inputted_number.append(number)
        filtered_list=set(inputted_number)
 
        if number!=filtered_list:
            print("Unique")
        else:
            print("Duplicate")
         
    except ValueError:
        print("!!INVALID INPUT!!")
        break
#display whether the number is unique or a duplicate