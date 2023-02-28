
class Laptop:
    def __init__(self,name,model,price):
        self.name = name
        self.model = model
        self.price = price
        self.details = "this is " + name + ' laptop is costs ' + price
    
lap1 = Laptop('dell','inspron133','56k')
lap2 = Laptop('hp','pavallien','90k')

print(lap1.model)
print(lap1.details)

