def remove(string,n):
    first=string[:n]
    last=string[n+1:]
    return first+last
string=input("enter a string:")
n=int(input("enter position for removing:"))
print("modified string is:",remove(string,n-1))