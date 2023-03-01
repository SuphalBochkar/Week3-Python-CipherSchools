
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

p1 = Person('suphal','bochkar',17)
p2 = Person('sai','bochkar',18)

# print(p1.full_name())
# print(Person.full_name(p1))
# print(p2.full_name())
# print(Person.full_name(p1))

# print(p1.adult())
