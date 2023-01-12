input1 = [True , False , [1,2,3] , 1, 1.0, 3] 
out = [str(i) for i in input1 if type(i) == int or type(i) == float]
print(out)
