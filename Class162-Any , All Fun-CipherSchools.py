
#& Any All Function

num1 = [2,4,6,8,10]
num2 = [1,2,3,4,5,6]

#& All
# print(all([1,1,1,1,1]))  #! ------> True
# print(all([1,1,2,1,1]))  #! ------> False

# print([i%2==0 for i in num1])
# print(all([i%2==0 for i in num1]))

#& Any
print(any([1,1,1,1,1]))  #! ------> True
print(any([7,5,2,1,3]))  #! ------> True
