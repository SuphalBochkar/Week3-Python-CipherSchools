# OBJECTIVES
# WHAT IS CLASS
# HOW TO CREATE AN CLASS
# WHAT IS INIT METHOD
# WHAT ARE ATTRIBUTES, INSTANCE VARIABLES
# HOW TO CREATE OUR OBJECT

class Person:
    def __init__(self,fn,ln,age):
        # instace variables
        print("init method is called")
        self.fn = fn
        self.ln = ln
        self.age = age

obj1 = Person('suphal','bochkar',18)
obj2 = Person('sai','bochkar',17)
print(obj1.fn)
print(obj2.fn)