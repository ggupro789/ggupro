def my_permutation(list,r,target):
    if len(target) == r:
        for item in target:
            print(item,end=' ')
        print()
        return
    
    for i in range(len(list)):
        if visited[i] == False:
            visited[i] = True
            my_permutation(list,r,target+[list[i]])
            visited[i]= False

N,M = map(int,input().split())
map = []
for i in range(N):
    map.append(i+1)
visited = [False for _ in range(N)]

my_permutation(map,M,[])
