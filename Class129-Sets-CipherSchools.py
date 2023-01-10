
#~ Sets
#~ On ordered means IndexError
# s = {1,2,3,4,1}
# print(s)
s = {1,2,3}

#~ remove dublicate
# list1 = [1,2,3,4,5,1,2,1,3,1,5,2]
# set1 = set(list1)
# print(set1)
# set1 = list(set(list1))
# print(set1)

#~ add elements to set
# s.add(2)
# s.add(1)
# s.add(3)
# s.add(4)
# s.add(5)
# print(s)

#~ deleting item
#! remove Item
removed = s.remove(3)
print(removed)               #! It only gives key
print(s)
#! discard Item
discarded = s.discard(5)
print(discarded)               #! It gives key and value
print(s)

s.clear()
