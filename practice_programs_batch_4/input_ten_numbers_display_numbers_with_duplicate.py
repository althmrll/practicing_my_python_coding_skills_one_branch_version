counter= 0
inputted_numbers= []

#ask user to input ten numbers
while counter!=10:
    print("numbers inputted:", counter)
    number_input= int(input("Enter number:"))
    counter=counter+1
    inputted_numbers.append(number_input)
 
#determine which inputs have duplicates
#print all numbers that have duplicates