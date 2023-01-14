# kwargs (keyword arguments)
# (**)kwargs (double star operator)

#~ kwargs as a parameter
# def fun(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# fun(f_n = 'suphal' , l_n = 'bochkar')

#! arguments should be in dictionary format
def fun(**kwargs):
    for k,v in kwargs.items():
        # print(f'key is {k} and value is {v}')
        print(f'{k} : {v}')
# fun(f_n = 'suphal' , l_n = 'bochkar')

#! taking One normal argument 
# def funt(a,**kwargs):
#     for k,v in kwargs.items():
#         # print(f'key is {k} and value is {v}')
#         print(f'{k} : {v}')
# fun('a',f_n = 'suphal' , l_n = 'bochkar')

#~ Dictionary unpacking
d = {'name' : 'Suphal ', 'age' : 18}
fun(**d)


