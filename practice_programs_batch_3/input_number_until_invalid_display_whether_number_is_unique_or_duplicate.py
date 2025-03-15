inputted_number= []
 
#input number(use while loop)
while True: #determine whether input is invalid
    try:
        number= int(input("Enter number:"))
        inputted_number.append(number)
         
    except ValueError:
        print("!!INVALID INPUT!!")
        break
#display whether the number is unique or a duplicate