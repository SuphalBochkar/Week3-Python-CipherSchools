
#~ Squares
# sq = [i**2 for i in range(1,11)]
# print(sq)

#~ If condition
# even_num = [i for i in range(1,11) if i%2 == 0]
# odd_num = [i for i in range(1,11) if i%2!=0]
# print(even_num)
# print(odd_num)

#~ if else condition
# e_sq_o_neg = [i*2 if i%2==0 else -i for i in range(1,11) ]
# print(e_sq_o_neg)

#~ nested list comprention
n = [[i for i in range(1,4)] for j in range(3)]
print(n)
