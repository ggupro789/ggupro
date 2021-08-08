number = int(input())
num = list(str(number))
get = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

for i in range(10):
    for j in range(0,len(num)):
        if(i == int(num[j])):
            get[i] +=1

for key in get.keys():
    if(key == 9):
        print(key)
    else:
        print(key,end=" ")

for value in get.values():
    print(value,end=" ")