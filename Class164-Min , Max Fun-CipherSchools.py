
#& Min() and Max()

# num = [1,2,3,4]
# print(max(num))
# print(min(num))

names  = ['suphal','bochkar','sai']
#! M-1
# print(max([len(i) for i in names]))
#! M-2
# print(max(names,key = lambda item : len(item)))
# print(sorted(names,key = lambda item : len(item),reverse=True))           #f2f #^ Most Important 

std1 = {
    'suphal' : {'score':100,'age':17},
    'bochkar' : {'score':60,'age':16},
    'sai' : {'score':99,'age':18}
}
print(max(std1,key = lambda item : std1[item]['score']))

std2 = [
    {'name':'suphal','score': 100,'age':17},
    {'name':'bochkar','score':60,'age':16},
    {'name':'sai','score':99,'age':18}
]
# print((max(std2,key = lambda item:item['score']))['name']) 
# print((max(std2,key = lambda item:item['age']))['name'])




