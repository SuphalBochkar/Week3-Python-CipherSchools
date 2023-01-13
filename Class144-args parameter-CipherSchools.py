
#* all arguments converted tuple
# def multi(*args):
#     mul = 1
#     for i in args:
#         mul *= i
#     return mul
# print(multi(1,2,3,4))

#* No Arguments
# def multi(*args):
#     mul = 1
#     print(a)
#     print(args)
#     for i in args:
#         mul *= i
#     return mul
# print(multi())

# *args with 1 normal parameter
# def multi(a,*args):
#     mul = 1
#     print(a)
#     print(args)
#     for i in args:
#         mul *= i
#     return mul
# print(multi(2,7,8,4))

# *args with 2 normal parameter
def multi(a,b,*args):
    mul = 1
    # print(a)
    print(args)
    for i in args:
        mul *= i
    return mul
print(multi(2,7))