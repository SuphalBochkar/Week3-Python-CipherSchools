# lambda expression practice

# def even_fun(a):
    #! M-1
    # if a%2==0:
    #     return True
    # return False
    #! M-2
#     return a%2 == 0
# print(even_fun(2))

# even = lambda a : a%2 == 0
# print(even(5))

# last_char = lambda a : a[-1]
# print(last_char('suphals'))

#~ lambda with if Else

def funv(s):
    #! M-1
    # if len(s) > 5:
    #     return True
    # return False
    #! M-2
    return len(s) > 5
print(funv('sai'))

fun = lambda s : True if len(s) > 5 else False
print(fun('suphal'))

fun2 = lambda s : len(s) > 5
print(fun2('suphal'))
