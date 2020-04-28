class laptop():

    def __init__(self):
        self.__maxprice=20000

    def sell(self):
        print("selling price of laptop is {}".format(self.__maxprice))

    def setmaxprice(self,price):
        self.__maxprice=price


c = laptop()
c.sell()

c.__maxprice=25000
c.sell()

c.setmaxprice(30000)
c.sell()

#check by using maxprice instead of __maxprice