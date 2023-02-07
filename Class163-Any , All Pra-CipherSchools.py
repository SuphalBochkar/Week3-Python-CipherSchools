def add(*args):
    if all([type(arg)==int or type(arg)==float for arg in args ]):
        return sum(args)
    return 'Wrong Man'

print(add(1,2,3,4,5.3,'suphal'))