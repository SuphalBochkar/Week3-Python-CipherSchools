def mul(*args):
    multi = 1
    print(args)
    for i in args:
        multi *= i
    return multi

nums = [2,3,4]
print(mul(*nums))     #! use (*) to unpack 
