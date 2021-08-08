def ox(x,y):
    sum =0
    for i in x:
        if(i == y):
            sum +=1
    
    if(sum == 1):
        return True
    else:
        return False

number = [2, 4, 6, 8, 10]
print("{0}\n{1} => {2}\n{3} => {4}".format(number,5,ox(number,5),10,ox(number,10))) 