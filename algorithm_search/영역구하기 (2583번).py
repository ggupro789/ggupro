def dfs(row,col,visited):
    global count

    visited[row][col] = 1
    count += 1
    stack = [(row,col)]

    dr = [0,0,-1,1]
    dc = [-1,1,0,0]

    while len(stack) > 0:
        row,col = stack.pop()

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]

            if 0<= nr < M and 0 <= nc <N:
                if visited[nr][nc] == 0 and map_list[nr][nc] == 0:
                    visited = dfs(nr,nc,visited)
    
    return visited


M,N,K = map(int,input().split())

map_list = [[0 for _ in range(N)]for _ in range(M)]

for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    for y in range(y1,y2):
        for x in range(x1,x2):
            map_list[y][x] = 1

visited = [[0 for _ in range(N)] for _ in range(M)]

area = 0
result_count = []

for row in range(M):
    for col in range(N):
        if map_list[row][col] == 0:
            if visited[row][col] == 0:

                count = 0
                dfs(row,col,visited)
                result_count.append(count)
                area += 1

print(area)

sorted_count = sorted(result_count,reverse=False)
for i in range(len(sorted_count)):
    if i == len(sorted_count):
        print(sorted_count[i])
    else:
        print(sorted_count[i],end=' ')