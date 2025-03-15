#input ten numbers
while True: #determines whether input is invalid
    try:
        number=int(input("Enter number:"))
     
    except ValueError:
        break
#print all inputted numbers except duplicates