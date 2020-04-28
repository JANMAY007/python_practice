numbers=int(input('Enter the totla numbers:'))
number=[]
for i in range(numbers):
    elem=int(input('Enter the element%d:'%(i+1)))
    number.append(elem)
avg=int(sum(number)/numbers)
print('The average is %d' %avg)