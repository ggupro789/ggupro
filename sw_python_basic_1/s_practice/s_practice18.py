x = 200
list = []
for i in range(200):
    if(i%7==0 and i%5 != 0):
        list.append(str(i))
list = ",".join(list)
print(list)