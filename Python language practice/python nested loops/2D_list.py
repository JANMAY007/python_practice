n=int(input("enter number of rows:"))
matrix = [[j for j in input().strip()] for i in range(n)]
print('\n')
print("your matrix is:")
for rows in matrix:
    for item in rows:
        print(item,end='',sep=' ')
    print()