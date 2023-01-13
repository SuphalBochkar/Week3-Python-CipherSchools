def to_pow(a,*args):
    if args:
        lis = []
        lis += [a**a]
        for i in args:
            lis += [i**a]
        return lis
    else :
        return ("hey u didi't pass bro ")
        
nums = [2,4,7]
out = to_pow(nums[0],*nums[1:])
print(out)

def to_pow(a,*args):
    if args:
        return  [i**a for i in args]
    else :
        return "hey u didi't pass bro "
        
nums = [2,4,7]
out = to_pow(nums[0],*nums[:])
print(out)

