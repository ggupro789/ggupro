
def dfs(row,col):
    global count

    visited = [[0 for _ in range(N)] for _ in range(M)]
    visited[row][col] = 1
    stack = [(row,col)]

    dr = [0,0,-1,1]
    dc = [-1,1,0,0]

    while len(stack) > 0:
        row,col = stack.pop()

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]

            if 0 <= nr < M and 0 <= nc < N:
                if map_list[nr][nc] < map_list[row][col]:
                    if visited[nr][nc] == 0:
                        if nr == M-1 and nc == N-1:
                            count += 1
                            return visited
                            
                        else:
                            visited[nr][nc] = 1
                            stack.append((nr,nc))
                            
    return visited

M,N = map(int,input().split())


map_list = []
for _ in range(M):
    map_list.append(list(map(int,input().split())))

count = 0

dfs(0,0)

print(count)




