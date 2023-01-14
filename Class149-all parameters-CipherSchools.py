# functions with all parameters
# very important to understand
# PADK

#f2f #! maintain order in PADK (parameters,args,DefaultPara,kwargs)
#~ parameters
# def pri(a):
#     print(a)

#~ default parameters
# def func(name = 'unknown',age=18):
#     print(name,age,sep='\n')    
# func(18)

def fun(name,*args,last_name = 'Bochkar',**kwargs):
    print(name,args,last_name,kwargs,sep='\n')

fun('suphal',1,2,3,a=1,b=2)

