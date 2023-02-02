# Filter Fun

def eve(a):
    return a%2==0

num =[1,2,4,7,3,5]
num1 =[1,2,4,7,3,5,6,8,12,46]



eve1 = list(filter(eve,num))
print(eve1)

eve2 = list(filter(lambda a:a%2==0,num1)) #! can be used cuz datatype is mentioned
print(eve2)

eve3 = (filter(lambda a:a%2==0,num1))     #! USed only ones datatype not mentioned
for i in eve3 : print(i)
for i in eve3 : print(i)


#~ LC
list_eve = [i for i in num if i%2==0]
print(f'hiii:    {list_eve}')

