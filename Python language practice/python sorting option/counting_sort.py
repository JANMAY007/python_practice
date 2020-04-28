def countingsort(array1,max_val):
    m=max_val+1
    count=[0]*m
    for a in array1:
        count[a]+=1
        i=0
        for a in range(m):
            for c in range(count[a]):
                array1[i]=a
                i+=1
    return array1
array1=list(map(int,input("enter elements: ").split()))
max_val=int(input("enter max value: "))
print(countingsort(array1,max_val))