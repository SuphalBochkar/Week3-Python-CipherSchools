# class methods
# difference between class methods and instance methods
#& Class-Varible Syntax
#^ Class_Name.varible = constant
#& Class-Method Syntax
#^ Class_Name.Method_Name()
class Person:
    #^ Class Variable / class attribuite
    count_instance = 0    

    def __init__(self,fn,ln,age):
        self.fn = fn
        self.ln = ln
        self.age = age
        Person.count_instance += 1
    
    #! cls ----> Class
    #! self ----> Object
    
    #^ Class Methods
    @classmethod            #^ Decorators
    def count_instances(cls):   
        return f"You have created {cls.count_instance} instances of {cls.__name__} class"

    #^ Instance Methods
    def full_name(self):   
        return f'He is {self.fn} {self.ln}'
    
    def adult(self):
        return self.age > 18

obj1 = Person('suphal','bochkar',18)   #^ Instance
obj2 = Person('sai','bochkar',17)



print(Person.count_instances())
