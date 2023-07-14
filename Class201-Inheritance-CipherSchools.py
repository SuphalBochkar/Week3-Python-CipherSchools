

class Phone:                #^ Base / Parent Class 
    def __init__(self,name,model,price):
        self.name = name                    
        self.model = model
        self._price = max(price,0)

    def full_name(self):
        return f'{self.name} {self.model}'
    
    def make_a_call(self,number):         
        print(f'Calling {number}...... form {self.name}')

