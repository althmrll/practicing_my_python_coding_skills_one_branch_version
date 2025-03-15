#input number(use while loop)
while True:
    try:
        number= int(input("Enter number:"))
         
    except ValueError:
        break
#display whether the number is unique or a duplicate
#determine whether input is invalid