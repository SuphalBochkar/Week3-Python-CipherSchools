class Laptop:
    discount = 10
    def __init__(self,brand,name,price):
        self.brand = brand
        self.name = name
        self.price = price  
    def offer(self):
        return f'Discount Price is {self.price - ((self.discount/100)*self.price)}'  #! to use objects discount if given

lap1 = Laptop('dell','inspron133',63000)
lap2 = Laptop('hp','pavallien',47000)
# print(lap1.__dict__)
print(lap2.__dict__)

# lap2.discount = 50
# print(lap2.offer())
