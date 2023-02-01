# Filter Fun

def eve(a):
    return a%2==0

num =[1,2,4,7,3,5]
num1 =[1,2,4,7,3,5,6,8,12,46]



eve1 = list(filter(eve,num))
print(eve1)
