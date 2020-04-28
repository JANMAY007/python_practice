n=int(input())
for i in range(1,n+1):
    for j in range(i-1):
        print(end=" ")
    value=i
    print(value,end=" ")
    temp=n
    for j in range(n-i):
        print(value+temp,end=" ")
        value+=temp
        temp-=1
    print()