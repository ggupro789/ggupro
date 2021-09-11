import math
def sosu(n):
    if n == 1:
        return False
    count = 0
    for i in range(1,int(math.sqrt(n))+1):
        if count > 2:
            return False
        if n%i == 0:
            count += 1
    
    return True

n = int(input())
k = int(input())

binary =''
bi2 = []
while n >0:
    n,mod = divmod(n,k)
    binary += str(mod)
binary =binary[::-1]

bi = binary.split("0")
bi = [i for i in bi if i]
print(bi)
if int(bi[0]) == int(binary):
    if sosu(int(bi[0])) == True:
        print(1)

for i in range(len(bi)):
    bi[i] = int(bi[i])

binary = int(binary)

for i in bi:
    if sosu(i) == True:
        bi2.append(i)

answer = len(bi2)
print(answer)




