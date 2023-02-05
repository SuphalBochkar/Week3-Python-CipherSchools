# # THIS IS CHALLENGE
# define a function take any
# return average
# ( 1+4+7 ) / 3
# try to make this
# anonymous
# no of lists containing number
# function in one line using lambda

#! M-1
# def ave1(l1,l2):
#     average = []
#     for pair in zip(l1,l2):
#         average.append(sum(pair)/len(pair))
#     return average
#! M-2
def ava2(*args):
    average = []
    for pair in zip(*args):
        average.append(sum(pair)/len(pair))
    return average
#! M-3
def ava3(*args):
    return [sum(pair)/len(pair) for pair in zip(*args)]
#! M-4
ava4 = lambda *args : [sum(pair)/len(pair) for pair in zip(*args)]

print(ava2([1,2,3],[4,5,6],[7,8,9]))
print(ava3([1,2,3],[4,5,6],[7,8,9]))
print(ava4([1,2,3],[4,5,6],[7,8,9]))