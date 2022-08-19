#Author: SAIMA NOOREEN
#Date:august 18, 2022
#initializing empty list
x=[]
y=[]
try:
    n=int(input("Enter the size of your list\n"))
    for i in range(n):
        #making separate variables for everything so that it would be easy
        t=int(input("enter your numbers "))
        x.append(t)
        if t>10:
            while True:
                t+=1
                p=str(t)
                if p==p[::-1]:
                    y.append(p)
                    break
                else:
                    continue
        else:
            y.append(t)
    print(y)
except Exception as e:
    print(e)
