import math
number = int(input("Enter any number: "))
#if number > 1:
for i in range(2, math.ceil(number**(1/2))):
    if (number % i) == 0:
        print(number, "is not a prime number")
        break
else:
    print(number, "is a prime number")
#else:
 #   print(number, "is not a prime number")
#9999999967