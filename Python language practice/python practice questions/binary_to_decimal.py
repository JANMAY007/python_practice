#method 1
n=int(input())
print(bin(n).replace("0b",""))

#method 2
def decimaltobinary(n):  
    if(n > 1):
        decimaltobinary(n//2)
    print(n%2, end='')
n=int(input())
#print(int(n,2))
decimaltobinary(n)