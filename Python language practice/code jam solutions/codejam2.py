import numpy as np
T = int(input())
for o in range(1,T+1):
  N = int(input())
  a = [[int(q) for q in input().split()] for p in range(0,N)]
  result = []
  x = np.trace(a)
  def func(a):
    count1=0
    for k in range(N):
      d = set(a[k])
      if len(d) < N:
        count1+=1
    return(count1) 
  result = list(map(list, zip(*a)))#transposing a  
  print ('%s #%d: %d %d %d' % ('Case',o,x,func(a),func(result)))