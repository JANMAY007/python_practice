import math
a=float(input("enter first side length:"))
b=float(input("enter second side length:"))
c=float(input("enter third side length:"))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("the area of so formed triangle is",area)
print("the area of so formed triangle is",round(area,2))