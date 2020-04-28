class Bulbul:

    def fly(self):
        print("bulbul can fly")

    def swim(self):
        print("bulbul can't swim")


class Ostriches:

    def fly(self):
        print("Ostriches can't fly")

    def swim(self):
        print("ostriches can swim")


def flying(bird):
    bird.fly()

blue=Bulbul()
red=Ostriches()
#blue.fly()
flying(blue)
flying(red)