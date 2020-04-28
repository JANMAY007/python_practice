#If the argument passed is in function then the whole is called as method
#first argument should be self if class is been used
class Greet:
    def method(self):
        print(f'Hi {name} !')
        print("Welcome here!!")
name=input()
Greet.method(name)