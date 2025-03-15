inputted_number=[]

#input number(use while loop)
#determine whether input is invalid

while True: #ensures the program continuously asks for input that stops when input is invalid
    try:
        number= int(input("Enter number:"))
        inputted_number.append(number)
         
    except ValueError:
        #print smallest number
        inputted_number.sort() #sorts list in ascending order
        print(inputted_number[0]) #prints first item on the list
        break