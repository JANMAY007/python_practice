string=input("enter a string: ")
sub_string=input("enter substring: ")
if(string.find(sub_string)==-1):
    print("substring not found!")
else:
    print("substring found!")