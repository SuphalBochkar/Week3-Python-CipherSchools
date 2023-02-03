
#& iterator vs iterales

num = [1,2,3,4]  #! Tuples, string -----> iterables
squares = map(lambda a:a*2,num)   #! Iterator



#& Iterables

num_iter = iter(num)
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))
# print(next(num_iter))

#& Iterator
print(next(squares))