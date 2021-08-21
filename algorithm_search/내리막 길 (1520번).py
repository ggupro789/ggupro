 보류
def dfs(row,col):
    global count
    global visited

    if visited[row][col] == 1:
        return visited
                    
    visited[row][col] = 1
    
    dr = [0,0,-1,1]
    dc = [-1,1,0,0]


    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]

        if 0 <= nr < M and 0 <= nc < N:
            if map_list[nr][nc] < map_list[row][col]:
                if nr == M-1 and nc == N-1:
                    count += 1
                    return visited
                    
                else:
                    visited = dfs(nr,nc)

    return visited

    
                            
    

M,N = map(int,input().split())

map_list = []
for _ in range(M):
    map_list.append(list(map(int,input().split())))

visited = [[0 for _ in range(N)] for _ in range(M)]

count = 0

dfs(0,0)
print(visited)
print(count)




