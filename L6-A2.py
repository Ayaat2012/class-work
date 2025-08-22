#Encapsulation is the concept of hiding inteernal data and requiring all interactions to be performed through an objects methods
class Computer:
    
    def __init__(self):
        self.__maxprice = 900 #private variable

    def sell(self):
        print("Selling Pricce: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

#trying to change the price
c.__maxprice = 1000
c.sell()

#using setter function
c.setMaxPrice(1000)
c.sell()