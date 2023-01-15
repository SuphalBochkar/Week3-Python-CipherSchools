# map function
num = [1,2,3,4]
names = ['abc','abcd','abcde']

#~ Basic
# new_lis = []
# for i in num :
#     new_lis += [i*i]
# print(new_lis)

#~ Defining
# def squ(a):
#     return a*a
# squares = list(map(squ,num))
# print(squares)

#~ Lambda and Map
# squares = list(map(lambda a:a*a,num))
# print(squares)

#~ LC
# squares1 = [i*i for i in num]
# print(squares1)

#~ Use map for predefined functions
length = map(len,names)             #! It can be used only once
for i in length :
    print(f'we canloop it {i}')
    print(f'whats happin {length}')
print(list(length))

length1 = list(map(len,names))             #! now it can be used 
for i in length :
    print(f'we canloop it {i}')
    print(f'whats happin {length}')
print(list(length))
