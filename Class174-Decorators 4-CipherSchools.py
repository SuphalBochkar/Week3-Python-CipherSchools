# output ----- >
# you are calling add
# This function takes function two numbers as parameters and return their sum
# 9

from functools import wraps

def print_func_data(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f'you are calling {function.__name__}')
        print(function.__name__)
        return function(*args, **kwargs)
    return wrapper
        
@print_func_data
def add(a,b):
    '''This function takes two numbers as arguments and return their sum'''
    return a+b
print(add(4,5))
