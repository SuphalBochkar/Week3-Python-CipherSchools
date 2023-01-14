names = ['suphal','bochkar']



#123 #~ My Code 
def func(name,**kwargs):
    if kwargs:
        return [i[-1].upper()+i[-2::-1] for i in name]
    else:
        return [i[0].upper()+i[1:] for i in name]

print('my',func(names))
print('my_rev',func(names,rev = True))

#f2f #~ Other Code        
def func(name,**kwargs):
    if kwargs.get('rev') == True:
        return [i[::-1].title() for i in name]
    else:
        return [i.title() for i in name]

print('other',func(names))
print('other_rev',func(names,rev = True))
