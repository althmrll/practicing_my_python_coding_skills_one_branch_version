numbers_inputted=[]

#Ask user ot input number until invalid
while True:
    try:
        number_input= int(input("Enter number:"))
        numbers_inputted.append(number_input)
    except ValueError:
        print(numbers_inputted)
 
#Print highest number