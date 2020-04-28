def selectionsort(nlist):
    for j in range(len(nlist)-1,0,-1):
        k=0
        for i in range(1,j+1):
            if(nlist[i]>nlist[k]):
                k=i
            temp=nlist[j]
            nlist[j]=nlist[k]
            nlist[k]=temp
    return nlist
nlist=input("enter elements: ").split()
print("the sorted list is:",selectionsort(nlist))