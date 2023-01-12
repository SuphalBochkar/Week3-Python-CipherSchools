
nums = list(range(1,11))
#~ if its odd do negative else *2 

new_nums = [i*2 if (i%2==0) else -i for i in nums] 
print(new_nums)
