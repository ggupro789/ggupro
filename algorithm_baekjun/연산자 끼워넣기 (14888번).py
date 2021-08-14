def dfs(i,start_v,plus,minus,mul,div): # DFS
    global maxi
    global mini
 
    if i == N:
        maxi = max(start_v,maxi)
        mini = min(start_v,mini)
        return

    else:
        if plus > 0:
            dfs(i+1,start_v+map_list[i],plus-1,minus,mul,div)

        if minus > 0:
            dfs(i+1,start_v-map_list[i],plus,minus-1,mul,div)

        if mul > 0:
            dfs(i+1,start_v*map_list[i],plus,minus,mul-1,div)

        if div > 0:
            dfs(i+1,int(start_v/map_list[i]),plus,minus,mul,div-1)



N = int(input())
map_list = tuple(map(int,input().split()))

plus, minus, mul, div = map(int,input().split())
all = [plus,minus,mul,div]

maxi = float('-inf')
mini = float('inf')

dfs(1,map_list[0],plus,minus,mul,div)

print(maxi)
print(mini)
