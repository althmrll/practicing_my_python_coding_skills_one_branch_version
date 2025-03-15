numbers_inputted=[]

#Ask user ot input number until invalid
while True:
    try:
        number_input= int(input("Enter number:"))
        numbers_inputted.append(number_input)
 
#Print highest number
    except ValueError:
        numbers_inputted.sort(reverse=True)
        print(numbers_inputted[0]) #prints highest number