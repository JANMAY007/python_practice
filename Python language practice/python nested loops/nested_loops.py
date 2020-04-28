T=int(input())
for i in range(T):
    N=int(input())
    M=[int(j) for j in input().split()]
count1=0
count2=0
count3=0
for i in range(T):
    for j in range(len(M)):
        if(j==M[0] or j==M[N-1]):
            count1+=1
        elif(M[j]>M[j-1] and M[j]>M[j+1]):
            count2+=1
        else:
            count3+=1
    for i in range(T):
        print("Case #%d: %d"%(T,count2))    