

#& Sort
# fru1 = ['grapes','mango','apple']
# fru1.sort()
# print(fru1)

#& Sorted ----> Tupul
# fru2 = ('grapes','mango','apple')
# print(sorted(fru2))

#& Sorted ----> Set
# fru3 = {'grapes','mango','apple'}
# print(sorted(fru3))

guitars = [
    {'model': 'yamaha', 'price' : 840},
    {'model': 'bez', 'price' : 112},
    {'model': 'yalchu', 'price' : 232},
    {'model': 'marge', 'price' : 781},
]
print(sorted(guitars,key = lambda d:d['price'],reverse=True))