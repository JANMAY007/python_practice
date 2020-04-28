n=int(input("Enter any number:"))
a=list(map(int,str(n)))
b=list(map(lambda x:x**3,a))
if(sum(b)==n):
    print("The number is armstrong.")
else:
    print("The number is not armstrong.")