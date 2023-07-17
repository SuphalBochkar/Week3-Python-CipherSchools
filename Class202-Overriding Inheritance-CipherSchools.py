# can we derive more than one class from base class ?
# multilevel inheritance
# method resolution order
# method overriding
# isinstance(), issubclass()
class Phone:    
    def __init__(self,name,model,price):
        self.name = name                    
        self.model = model
        self._price = max(price,0)
    def full_name(self):
        return f'1 : {self.name} first {self.model}'
    def make_a_call(self,number):         
        print(f'Calling {number}...... form {self.name}')

class Smartphone(Phone):
    def __init__(self, name, model, price,ram,memory,f_cam):
        super().__init__(name, model, price)
        self.ram = ram
        self.memory = memory
        self.f_cam = f_cam
    def full_name(self):
        return f'2 : {self.name} {self.model} it costs second {self._price}' 
    
class FlagshipPhone(Smartphone):
    def __init__(self,name, model, price,ram,memory,f_cam,r_cam):
        super().__init__(name, model, price,ram,memory,f_cam)
        self.f_cam = f_cam
        self.r_cam = r_cam
    def full_name(self):
        return f'3 : {self.name} {self.model} it costs second {self._price}'

