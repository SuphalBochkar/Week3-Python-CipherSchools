
class Person:
    def __init__(self,fn,ln,age):
        self.fn = fn
        self.ln = ln
        self.age = age
    
    def full_name(self):
        return f'He is {self.fn} {self.ln} of {self.age} years'
    
    def adult(self):
        if self.age > 18:
            return 'You big man'
        return "Smoll"
