

l1 = [1,3,5,7]
l2 = [2,4,6,8]
l = [(1,2),(3,4),(5,6),(7,8)]   #! Goal

# * operator with zip

# print(list(zip(*l)))
# l1,l2 = zip(*l)
# print(list(l1))
# print(l2)

maxq = []
for pair in zip(l1,l2):
    maxq += [max(pair)]
print(maxq)


