def dfs(row,col,visited,count):
    visited[row][col] = 1

    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                if map_list[i][j] == 0:
                    count += 1
                    visited = dfs(i,j,visited,count)

    return count
    
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
                dfs(row,col,visited)
                area += 1
print(count)