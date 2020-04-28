def range_prod(lo,hi):
    if lo+1 < hi:
        mid = (hi+lo)//2
        return range_prod(lo,mid) * range_prod(mid+1,hi)
    if lo == hi:
        return lo
    return lo*hi

def treefactorial(n):
    if n < 2:
        return 1
    return range_prod(1,n)
n = int(input())
b=[]
def prime(x):
	prime = []
	for p in range(2, 10000):
		for q in range(2, p):
			if p % q == 0:
				break
		else:
			prime.append(p)
		if len(prime) == x:
			return prime
for i in prime(n):
  b.append(i)		
#print(b)
t = 0
for i in range(len(b)):
  t = t + treefactorial(b[i])
print(t)
if t%16==0:
  print(True)
else:
  print(False)