class Phone:
    def __init__(self,name,model,price):
        self.name = name                    
        self.model = model
        self._price = max(price,0)

    @property
    def speci(self):
        return f'{self.name} {self.model} is price of {self._price}'
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,new_price):
        self._price = max(new_price,0)
    
    def make_a_call(self,number):         
        print(f'Calling {number}...... form {self.name}')
    
    def full_name(self):
        return f'{self.name} {self.name}'


pho1 = Phone('Nokia','1100',1000)

# print(pho1.name)
# print(pho1.model)
pho1._price = -500
print(pho1.price)
print(pho1.speci)
