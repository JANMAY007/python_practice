numbers=list(map(int,input().split()))
print(numbers)
numbers.insert(0,18)
print(numbers)
print(numbers.index(5))
print(3 in numbers)
print(numbers.count(1))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
unique=[]
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)