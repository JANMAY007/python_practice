def make_awesome(func):
    def inner():
        print("i'm decorated")
        func()
    return inner

@make_awesome
def ordinary():
    print("i'm ordinary")

ordinary()
#awesome=make_awesome(ordinary)
#awesome()