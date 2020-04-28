number=int(input('Enter the number whose smallest divisor you want:'))
divisor=[]
for i in range(1,number+1):
    if(number%i==0):
        divisor.append(i)
divisor.sort()
print("The smallest divisor of %d is %d."%(number,divisor[0]))