#for particular number
n=int(input("enter nmber of elements:"))
a=[]
for i in range(1,n+1):
    b=int(input("enter %d element:"%i))
    a.append(b)
num=int(input("enter the number to be counted:"))
k=0
for j in a:
    if(j==num):
        k+=1
print("number",num,"repeats",k,"times.")