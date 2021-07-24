# result = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5}

alpha = 'abcdef'
number = [0,1,2,3,4,5]

result = dict(zip(alpha,number))
for key,value in result.items():
    print("%c: %d"%(key,value))
