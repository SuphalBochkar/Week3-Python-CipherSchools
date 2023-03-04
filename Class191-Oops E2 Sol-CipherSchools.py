

class Laptop:
    def __init__(self,brand,name,price):
        self.brand = brand
        self.name = name
        self.price = price
    
    def discount(self):
        # a = int(input())
        return f'Discount Price is {self.price - ((int(input())/100)*self.price)}'

lap1 = Laptop('dell','inspron133',63000)
# lap2 = Laptop('hp','pavallien',47000)

print(lap1.discount())
# print(lap2.discount())

