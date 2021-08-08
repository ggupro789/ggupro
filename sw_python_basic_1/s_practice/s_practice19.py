
list = []

for i in range(100,301):
    if(int(i/10)%2 == 0 and int(i/100)%2 == 0 and i%2 == 0):
        list.append(str(i))
list = ",".join(list)
print(list)