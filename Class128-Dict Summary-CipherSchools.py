# Summary

#* To Represent
d = {'name' : 'Suphal','age' : 18}
# d1 = dict(name = 'Suphal',age = 18)
# d2 = {
#     'name' : 'suphal',
#     'age' : 18 ,
#     'fav_movies' : [],
# }

#~ TO acess
# print(d['name'])

#~ add items to dict
# empty = {}
# print(empty)
# empty['key1'] = 'val1'
# empty['key2'] = 'val2'
# print(empty)

#~ To check
# if 'name' in d :
#     print("It exits")

#~ Iteration
# for key,val in d.items():
#     print(f'key is {key} and value is {val}')

#~ To print all Keys
# for i in d:
#     print(i)
# for i in d.keys():
#     print(i)
    
#~ To print all Keys
# for i in d.values():
#     print(i)

#~ Get method
#! if that particular key exists
# print(d.get('name'))
# print(d['name'])
#! if that particular key not exists
# print(d.get('names'))               #! it gves none
# print(d['names'])                   #! it gives error

#~ Deleting item
#! Pop Item
# popped = d.pop('name')
# print(popped)               #! It only gives key
# print(d)
#! Popped Item
# popped = d.popitem()
# print(popped)               #! It gives key and value
# print(d)


