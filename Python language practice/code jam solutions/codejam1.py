import random
import numpy as np
def createMat(n):
    ftRow = random.sample(range(n),n)
    perm = random.sample(range(n),n)
    return list(ftRow[i:]+ftRow[:i] for i in perm)
def func(m,K):
  global j
  m = createMat(N)
  y = sum( m[x][x] for x in range(N) )
  if y == K:
    print("Case #"+str(j)+": POSSIBLE")
    for i in m:
        print(' '.join(map(str,i)))
  else:
    func(m,K)
    #print("Not possible")

n = int(input())
arr2d = [[j for j in input().strip()] for i in range(n)] 
    #print(arr2d)
j=1
for i in arr2d:
    N = int(i[0])
    K = int(i[2])
    m = createMat(N)
    try:
      func(m,K)
    except RecursionError as re:
        print('Case #'+str(j)+': IMPOSSIBLE')
    j = j+1