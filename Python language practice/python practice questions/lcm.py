a=int(input("enter first number:"))
b=int(input("enter second number:"))
if(a<b):
    min=b
else:
    min=a
while 1:
    if(min%a==0 and min%b==0):
        print("L.C.M =",min)
        break
    min+=1