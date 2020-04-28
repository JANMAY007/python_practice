n = int(input())
o = (2 * n) - 2
for i in range(1, n+1):
    for j in range(0, o):
        print(end=" ")
    o = o + 1 
    for j in range(0, i):
        print(i, end=' ')
    print(" ")