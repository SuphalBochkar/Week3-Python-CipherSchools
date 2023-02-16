
#^ @ is used as decorator

def deco_func(any_func):
    def wrapper():
        print('This is awesome Function')
        any_func()
    return wrapper
