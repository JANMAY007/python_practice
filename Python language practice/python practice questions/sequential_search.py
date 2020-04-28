def sequential_search(dlist,item):
    pos=0
    found=False
    while(pos<len(dlist) and not found):
        if(dlist[pos]==item):
            found=True
        else:
            pos+=1
    return(found,pos)
arr=input("enter elements:").split()
n=input("enter element for search:")
print(sequential_search(arr,n))