letter=['a','b','c','d']
print(letter)#1
for i in range(len(letter)):
    print(letter[i],end='')
print('\n',letter[1:4])
print('\n',letter[::2])
print('\n',letter[2::])
print(letter[:])#it is same as 1