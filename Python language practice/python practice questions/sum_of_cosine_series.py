import math
def cosine(x,n):
    cos=1
    sign=-1
    for i in range(2,int(n),2):
        pi=3.14159
        y=x*(pi/180)
        cos=cos+(sign*(y**i))/math.factorial(i)
        sign=-sign
    return cos
x=float(input("enter the value of x in degrees:"))
n=float(input("enter the number of terms:"))
print(cosine(x,n))