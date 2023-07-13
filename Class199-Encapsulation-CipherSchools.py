# Encapsulation
# Abstraction
# Some special naming convention
# Name mangling

class Phone:
    def __init__(self,name,model,price):
        self.name = name                    #^ Encapulation 
        self.brand = model
        # self._price = price
        self.__price = price
    
    def make_a_call(self,number):         
        print(f'Calling {number}...... form {self.name}')
    
    def full_name(self):
        return f'{self.name} {self.name}'
    
    def send_msg(self):
        pass   # Twilio

# _name #! Convention of private message
# __name__ #! Dunder / magic methods
# l = [3,4,1,2]
# l.sort()   #^ tim Sort              #^ Hiding DAta in BAckground [Abstraction] hiding complexity

phone1 = Phone('nokia','1100',1000)
print(phone1.__dict__)
phone1._Phone__price = -1000
print(phone1._Phone__price)


