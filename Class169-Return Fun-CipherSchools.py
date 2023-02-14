
def outer_fnc():
    def inner_fnc():
        print('Inside Function')
    return inner_fnc
# var = outer_fnc
# var()

def outer_fnc2(msg):
    def inner_fnc2():
        print(f'your message is : {msg}')
    return inner_fnc2
var2 = outer_fnc2('ksdfhkk')
var2()
