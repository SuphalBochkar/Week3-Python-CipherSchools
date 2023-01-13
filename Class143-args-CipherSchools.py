# make flexible functions
# *operator
# *args

# def total(a,b):
#     return a+b
# print(total(3,4))

def all_total(*args):
    tot = 0
    for i in args:
        tot += i
    return tot
print(all_total(1,2,3,4,5,6,7))

    