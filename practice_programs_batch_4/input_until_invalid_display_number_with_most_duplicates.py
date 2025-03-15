inputted_numbers=[]
highest_duplicate_count=0

#Ask user to input number until invalid number.
while True:
    try:
        number_input= int(input("Enter number:"))
        inputted_numbers.append(number_input)
 
 #Determine which numbers are duplicates and the highets duplicate count
        inputted_numbers.count (number_input)
        if inputted_numbers.count (number_input)>highest_duplicate_count:
            highest_duplicate_count= number_input
        else:
            continue

#Print number with the most duplicates.