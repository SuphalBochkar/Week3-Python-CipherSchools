
def add(a,b):
    return a+b 
print(add(1,4))

#~ *args        ---Its Tuple---
# def fun(*args):
#     tot = 0
#     for i in args:
#         tot += i
#     return tot
# print(fun(1,2,3,4,5))

#~ To unpack
# l = [1,2,3,4,5]
# print(fun(*l))

#~ **kwargs    ---Its Dictionary---
# def func(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# func(a=3,b=3,c=6,d=7)

#! Order Of the paramaeters
#* PADK
#& Parameter ,*args , Default Parameter, **kwargs
