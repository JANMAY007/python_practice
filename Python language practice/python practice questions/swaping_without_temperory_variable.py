number1=int(input("Enter first number:"))
number2=int(input("Enter second number:"))
print("Original numbers:%d  %d"%(number1,number2))
number2=number1+number2
number1=number2-number1
number2=number2-number1
print("After swaping:%d  %d"%(number1,number2))