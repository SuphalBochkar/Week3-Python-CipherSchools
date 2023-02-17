
#^ @ is used as decorator

def deco_func(any_func):
    def wrapper():
        print('This is awesome Function')
        any_func()
    return wrapper

@deco_func
def func1():
    print('this is function one 1')
func1()

@deco_func
def func2():
    print('this is function one 2')
func2()
    
var1 = deco_func(func1)
var1()
var2 = deco_func(func2)
var2()