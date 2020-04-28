lower=int(input("Enter the lower range:"))
upper=int(input("Enter the upper range:"))
for i in range(lower,upper+1):
    summation=[]
    for j in range(1,i+1):
        print(j,sep=' ',end=' ')
        if(j<i):
            print("+",sep=" ",end=" ")
        summation.append(j)
    print("=",sum(summation))