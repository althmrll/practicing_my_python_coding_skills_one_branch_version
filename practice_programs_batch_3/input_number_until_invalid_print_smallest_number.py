#input number(use while loop)
#determine whether input is invalid

while True: #ensures the program continuously asks for input that stops when input is invalid
    try:
        number= int(input("Enter number:"))
         
    except ValueError:
        break
#print smallest number