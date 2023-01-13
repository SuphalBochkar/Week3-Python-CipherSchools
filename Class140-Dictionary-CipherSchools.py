
#~ dictionary comprehension

# square = {1:1, 2:4, 3:9}

#! Simple
# sq = {i:i**2 for i in range(1,4)}
# print(sq)

#! Modified
# sq1 = {f'Square of {i} is':i*i for i in range(1,11)}
# print(sq1)
# for k,v in sq1.items():
#     print(f'{k} : {v}')

#~ Word Count
s = 'Suphalllas'
count = {i:s.count(i) for i in s}
print(count)