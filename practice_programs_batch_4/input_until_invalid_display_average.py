count=0
total=0

#Ask user to input number continuously
while True:
    try:
        number= int(input("Enter number:"))
# Find their average
    #Add all the numbers together
        total= total+number #Add all the numbers together
        count=count+1 #Count the number of numbers inputted
 
    except ValueError:
        average= total/count #Divide the total of numbers to the count of numbers inputted
        print(round(average,2)) #Print their average