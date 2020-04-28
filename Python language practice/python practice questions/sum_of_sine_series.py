import math
def sine(x,n):
    sine=0
    for i in range(int(n)):
        sign=(-1)**i
        pi=3.14159
        y=x*(pi/180)
        sine=sine+((y**(2.0*i+1))/math.factorial(2*i+1))*sign
    return sine
x=float(input("enter the value of x in degrees:"))
n=float(input("enter the number of terms:"))
print(sine(x,n))