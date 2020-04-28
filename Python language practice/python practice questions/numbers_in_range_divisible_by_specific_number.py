lower=int(input("Enter the lower range:"))
upper=int(input("Enter the upper range:"))
specific_number=int(input("Enter the number whose multiple you want in range:"))
for i in range(lower,upper+1):
    if(i>=specific_number):
        if(i%specific_number==0):
            print(i)