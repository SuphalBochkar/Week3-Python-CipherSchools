# Encapsulation
# Abstraction
# Some special naming convention
# Name mangling

phone1 = Phone('nokia','1100',1000)
print(phone1.__dict__)
phone1._Phone__price = -1000
print(phone1._Phone__price)


