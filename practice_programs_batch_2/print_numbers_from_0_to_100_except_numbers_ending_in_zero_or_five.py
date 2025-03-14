#Print numbers from 0-100 except those ending in zero or five
for i in range (0, 101):
    if i%5==0 or i%10==0:
        print(i)