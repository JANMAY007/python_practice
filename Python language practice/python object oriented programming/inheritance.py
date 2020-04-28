#ability of parent class can be given to chlid class
#the function method are same in all class
#try in other way by understanding this code
class mammal:

    def speak(self):   #
        print("all mammal speak")


class dog:

    def speak(self):    #
        print("so dogs also speak")


class cat:

    def speak(self):    #
        print("but cat sleeps more")


mammals=mammal()
mammals.speak()

puppy=dog()
puppy.speak()

kitten=cat()
kitten.speak()