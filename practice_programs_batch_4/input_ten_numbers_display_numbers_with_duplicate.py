counter= 0
inputted_numbers= []
dupes=[]

#ask user to input ten numbers
while counter!=10:
    print("\nnumbers inputted:", counter)
    number_input= int(input("Enter number:"))
    inputted_numbers.append(number_input)
    counter=counter+1
 
#determine which inputs have duplicates
    if inputted_numbers.count(number_input)>1:
        dupes.append(number_input)
 
#print all numbers that have duplicates
number_with_dupes=set(dupes)
print(number_with_dupes)