# OBJECT ORIENTED PROGRAMMING
# COMMON TOPIC IN ALMOST ALL POPULAR PROGRAMING LANGUAGES(PYTHON,
# WITH COMMON IDEA BUT WITH DIFFERENT SYNTAX
# OOP IS JUST A STYLE/WAY TO WRITE A CODE
# VERY HELPFUL IN CREATING REAL WORLD PROGRAMS
# JAVA)
# # WE WILL
# class
# SEE OTHER ADVANTAGES WHEN WE WILL START LEARNING OOP

# wject(instance), method

# list class   
# list object
# method


l = [1,2,3,4]
l1 = [5,6,7,8]
l3 = ['suphal','sai']
l.append(8)



 

class List:
    def __init__(self,l):
        self.list = list
l = List(1,2,3,4)

class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
    def details(self):
        return f'{self.brand} {self.color}'
obj = Car('benz','black')    
print(obj.details())







