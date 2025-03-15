#input number(use while loop)
while True: #determines whether input is invalid
    try:
        number=int(input("Enter number:"))
     
    except ValueError:
        break
#sort all inputted numbers in ascending order