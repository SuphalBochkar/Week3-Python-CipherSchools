
#* ----------- A -----------
class A:
    def class_a_method(self):
        return 'I\'m just a class a method'
    def hello(self):
        return 'Hello form class A'
instance_a = A()
# print(instance_a.class_a_method())
#* ----------- B -----------
class B:
    def class_b_method(self):
        return 'I\'m just a class b method'
    def hello(self):
        return 'Hello form class B'
instance_b = B()
# print(instance_b.class_b_method())
#* ----------- C -----------
class C(A,B):
    pass
instance_c = C()
# print(instance_c.class_a_method())
# print(instance_c.class_b_method())
# print(instance_c.hello())
# print(help(C))
print(C.mro())        #^ List
print(C.__mro__)      #^ Tuple








