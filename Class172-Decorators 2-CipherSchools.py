def deco_func(any_func):
    def wrapper(*args, **kwargs):
        print('This is awesome Function')
        return any_func(*args, **kwargs)
    return wrapper

@deco_func
def func(a):
    print(f'this is a function eith an argument {a}')
func(2)
