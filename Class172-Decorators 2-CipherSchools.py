def deco_func(any_func):
    def wrapper(*args, **kwargs):
        print('This is awesome Function')
        return any_func(*args, **kwargs)
    return wrapper

@deco_func
def func(a):
    print(f'this is a function eith an argument {a}')
func(2)

@deco_func
def add(a,b):
    return a+b
print(add(2,3))


