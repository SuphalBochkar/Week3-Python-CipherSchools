from functools import wraps

def deco_func(any_func):
    @wraps(any_func)
    def wrapper(*args, **kwargs):
        ''' This is wrapper Function'''
        print('This is awesome Function')
        return any_func(*args, **kwargs)
    return wrapper

@deco_func
def add(a,b):
    ''' This is add Function'''
    return a+b

print(add.__doc__)
print(add.__name__)
