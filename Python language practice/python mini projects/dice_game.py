import random

def roll():
    first=random.randint(1,6)
    second=random.randint(1,6)
    return(first,second)

print(roll())