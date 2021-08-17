def dfs(row,col,visited,count):
    visited[row][col] = 1
    dr = [0,0,-1,1]
    dc = [-1,1,0,0]

    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        
    
M,N,K = map(int,input().split())

map_list = [[0 for _ in range(M)]for _ in range(N)]

for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    for y in range(y1-1,y2-1):
        for x in range(x1-1,x2-1):
            map_list[y][x] = 1

visited = [[0 for _ in range(M)] for _ in range(N)]

area = 0

for row in range(N):
    for col in range(M):
        if map_list[row][col] == 0:
            if visited[row][col] == 0:
                dfs(row,col,visited,0)
                area += 1
print(count)