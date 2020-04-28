lower=int(input("Enter the lower range:"))
upper=int(input("Enter the upper range:"))
summation=[]
for i in range(lower,upper+1):
    print(i,sep=' ',end=' ')
    if(i<upper):
        print("+",sep=" ",end=" ")
    summation.append(i)
print("=",sum(summation))