def insertionsort(nlist):
    for i in range(1,len(nlist)):
        currentvalue=nlist[i]
        position=i
        while(position>0 and nlist[position-1]>currentvalue):
            nlist[position]=nlist[position-1]
            position-=1
        nlist[position]=currentvalue
    return nlist
nlist=input("ener elements: ").split()
print(insertionsort(nlist))