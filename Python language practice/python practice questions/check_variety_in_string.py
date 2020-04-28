string=input("enter a string :")
count1=0
count2=0
count3=0
count4=0
for i in string:
    if(i.islower()):
        count1+=1
    elif(i.isupper()):
        count2+=1
    elif(i.isdigit()):
        count3+=1
    elif(i.isalnum()):
        count4+=1
#more variety are available for i.isxxxx()
print("lowercase letters are",count1)
print("uppercase letters are",count2)
print("digits are",count3)
print("alphanumerics are",count4)