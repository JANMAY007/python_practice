n=int(input())
reversed_number=0
while(n!=0):
    reversed_number=reversed_number*10 + n%10
    n=n//10
print(reversed_number)