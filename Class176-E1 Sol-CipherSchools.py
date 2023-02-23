from functools import wraps
import time

def calculator_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Excuting........{func.__name__}')
        t1 = time.time()
        value = func(*args, **kwargs)
        t2 = time.time()
        print(f'this programe took {t2-t1} seconds to execute')
        return value
    return wrapper

@calculator_time
def square(n):
    return [i**2 for i in range(1,n+1)]
square(99999999)