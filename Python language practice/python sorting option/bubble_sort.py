def bubblesort(nlist):
    for j in range(len(nlist)-1,0,-1):
        for i in range(j):
            if(nlist[i]>nlist[i+1]):
                temp=nlist[i]
                nlist[i]=nlist[i+1]
                nlist[i+1]=temp
    return nlist
nlist=input("enter elements: ").split()
print("the sorted list is:",bubblesort(nlist))