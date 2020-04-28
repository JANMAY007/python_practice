def my_program():
    n=1
    yield n
    print("this is first")
    #yield n
    n+=1
    yield n
    print("this is second")
    #yield n
    n+=1
    yield n
    print("this is third")
    #yield n

for item in my_program():
    print(item)