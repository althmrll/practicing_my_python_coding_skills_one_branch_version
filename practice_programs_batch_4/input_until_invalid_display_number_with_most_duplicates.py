inputted_numbers=[]
most_duplicated=0
#Ask user to input number until invalid number.
while True:
    most_duplicated=inputted_numbers.count (number_input)
    try:
        number_input= int(input("Enter number:"))
        inputted_numbers.append(number_input)
 
 #Determine which numbers are duplicates and the highets duplicate count
        inputted_numbers.count (number_input)
        print(inputted_numbers.count (number_input))
        if inputted_numbers.count(number_input)>inputted_numbers.count(most_duplicated):
            most_duplicated= number_input
        else:
            continue

#Print number with the most duplicates.
    except ValueError:
        print ("The most duplicated number is", most_duplicated)