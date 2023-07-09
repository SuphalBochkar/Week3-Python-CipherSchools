class Person:
    count_instance = 0    
    def __init__(self,fn,ln,age):
        self.fn = fn
        self.ln = ln
        self.age = age
        Person.count_instance += 1
    
    @classmethod
    def from_string(cls,string):
        f,l,a = string.split(",")
        return cls(f,l,a)
    
    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instance} instances of {cls.__name__} class"
        
        
    def full_name(self):   
        return f'He is {self.fn} {self.ln}'
        
    def adult(self):
        return self.age > 18
p1 = Person('suphal','bochkar',18)   
p2 = Person('sai','bochkar',17)

p3 = Person.from_string('sai,bochkar,20')
print(p3.full_name())