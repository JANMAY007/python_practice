lower=int(input("Enter the lower limit of odd numbers:"))
upper=int(input("Enter the upper limit of odd numbers:"))
for i in range(lower,upper+1):
    if(i%2!=0):
        print(i)