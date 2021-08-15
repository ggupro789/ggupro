def my_combination(list,k,r,target):
    if len(target) == r:
        result.append(sorted(target))
        return

    if k >= len(list):
        return
    
    my_combination(list,k+1,r,target)
    my_combination(list,k+1,r,target+[list[k]])

N,M = map(int,input().split())
map = []
for i in range(N):
    map.append(i+1)
result = []

my_combination(sorted(map,reverse=True),0,M,[])

result = sorted(result)

for i in range(len(result)):
    for j in range(M):
        print(result[i][j], end=' ')
    print()