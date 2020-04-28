def remove(string):
    first=""
    for i in range(len(string)):
        if (i%2==0):
            first=first+string[i]
    return(first)
string=input("enter a string:")
print("modified string is:",remove(string))