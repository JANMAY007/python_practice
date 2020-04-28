n=int(input("enter a number:"))
temp=n
sum=0
while n:
    r=n%10
    i=1
    f=1
    while i<=r:
        f=f*i
        i=i+1
    sum=sum+f
    n=n//10
if(sum==temp):
    print("number is a strong number.")
else:
    print("number is not a strong number.")