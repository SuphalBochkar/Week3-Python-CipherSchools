# We use enumerate function with for loop to track position of our item in iterable

names = ['suphal','sai','bochkar']

#~ How we can do this without enumerate function
# pos = 0
# for i in names :
    # print(f'{pos} ----> {i}')
#     pos += 1

#~ with enumerate function
# for pos , name in enumerate(names):
#     print(f'{pos} ----> {name}')

def check(l,s):
    for i,j in enumerate(l):
        if j == s:
            return i
    return -1
print(check(names,'bochkar'))

    