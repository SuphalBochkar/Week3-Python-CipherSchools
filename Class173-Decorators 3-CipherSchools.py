from functools import wraps

def deco_func(any_func):
    @wraps(any_func)
    def wrapper(*args, **kwargs):
        ''' This is wrapper Function'''
        print('This is awesome Function')
