n=int(input("enter the number of elements to be in the list:"))
b=[]
for i in range(0,n):
    a=int(input("element%d:"%(i+1)))
    b.append(a)
c=[]
d=[]
for i in b:
    if(i%2==0):
        c.append(i)
    else:
        d.append(i)
c.sort()
d.sort()
count1=0
count2=0
for j in c:
    count1+=1
for k in d:
    count2+=1
print("largest even number is:",c[count1-1])
print("largest odd number is:",d[count2-1])