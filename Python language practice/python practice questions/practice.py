n = int(input())
#-1/2 * (n**2 -15*n + 12)
o = -1/2 * (n**2 -15*n + 12)
for i in range(1, n+1):
    for j in range(0, i):
        print(-1/2 * ((n+j)**2 -15*(n+j) + 12), end=' ')
    for j in range(0, int(o)):
        print(end="")
    o = o + 1 
    print(" ")
