count=0
inputted_number=[]

#Ask user ot input number until invalid
while True:
    try:
        number_input= int(inout("Enter number:"))
        count=count+1
        inputted_number.append(number_input)
#print numbers in descending order