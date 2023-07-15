

class Phone:                #^ Base / Parent Class 
    def __init__(self,name,model,price):
        self.name = name                    
        self.model = model
        self._price = max(price,0)

    def full_name(self):
        return f'{self.name} {self.model}'
    
    def make_a_call(self,number):         
        print(f'Calling {number}...... form {self.name}')

class Smartphone(Phone):         #^ Derived / Child Class

    def __init__(self, name, model, price,ram,memory,cam):

        # Phone.__init__(self,name,model,price)
        super().__init__(name, model, price)
        self.ram = ram
        self.memory = memory
        self.cam = cam

phone1 = Phone('nokia','1100',1000)
smart1 = Smartphone('onePlus','note 10',3000,'6 GB','128 GB','20 MP')
print(phone1.full_name())
print(smart1.full_name() + f' and price is {smart1.cam}')

