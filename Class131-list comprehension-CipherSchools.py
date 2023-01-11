
#~ Normal Method
# sq1 = []
# for i in range(1,11):
#     sq1 += [i**2]
# print(sq1)
#~ List Comprention
# sq2 = [i**2 for i in range(1,11)]    
# print(sq2)

# nega = []
# for i in range(1,11):
#     nega += [-i]
# print(nega)
#~ LC
# nega1 = [-i for i in range(1,11)]
# print(nega1)

#~ Normal Method
names = ['suphal' , 'sai' , 'bochkar']
lis1 = []
for i in names:
    lis1 += [i[0]]
print(lis1)
#~ LC
lis2 = [i[0] for i in names]
print(lis2)
