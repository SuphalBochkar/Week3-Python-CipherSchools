
#~ Circle
# class Circle:
#     pi = 3.14
#     def __init__(self,radius):
#         self.radius = radius    
#     def circum(self):
#         return 2*Circle.pi*self.radius
#     def area(self):
#         return Circle.pi*(self.radius**2)
# obj1 = Circle(5)
# obj2 = Circle(7)
# print(obj1.circum())
# print(obj2.circum())
# print(obj1.area())
# print(obj2.area())

#~ Laptop
class Laptop:
    discount = 10
    def __init__(self,brand,name,price):
        self.brand = brand
        self.name = name
        self.price = price  
    def offer(self):
        return f'Discount Price is {self.price - ((Laptop.discount/100)*self.price)}'
lap1 = Laptop('dell','inspron133',63000)
lap2 = Laptop('hp','pavallien',47000)
print(lap1.offer())
# print(lap2.discount())
