def func(n):
  if n<=1:
    return n
  else:
    return(func(n-1) + func(n-2))
n = int(input())
for k in range(1,n+1):
  print(func(k))