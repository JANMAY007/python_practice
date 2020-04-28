#random module package
import random

members=["test","heros","krish","singer",]

for i in range(3):
    print(random.randint(10,20))

print(random.choice(members))



#datetime module package
from datetime import date

today=date.today()

print(today)
print(today.year)
print(today.month)
print(today.day)



#timing the code
import timeit

def my_func():
    y=3.14159
    for i in range(100):
        y=y**0.7
    return y

print(timeit.timeit(my_func,number=100000))



#regular expression
import re

bar="Hindustan is the best!"
a1=re.search("^Hindustan.*best!$",bar)
a2=re.findall("Hindustan",bar)
a3=re.split("\s",bar)
a4=re.sub("\s","@",bar)

if a1:
    print("matched")
else:
    print("not matched")
    
print(a2)
print(a3)
print(a4)