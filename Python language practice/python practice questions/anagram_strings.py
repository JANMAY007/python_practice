string1=input("enter first string:")
string2=input("enter second string:")
if sorted(string1)==sorted(string2):
    print("strings are anagrams.")
else:
    print("strings are not anagrams.")