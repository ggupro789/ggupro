import collections

def bfs(row,col):
    global r,c

    deq = collections.deque()
    deq.append((row,col))
    visited[row][col] = True
    dr = [0,0,-1,1]
    dc = [-1,1,0,0]

    while len(deq) > 0:
        row,col = deq.popleft()

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]

            if 0 <= nr < M and 0 <= nc < N:
                if map_list[nr][nc] != '#':
                    if visited[nr][nc] == False:
                        visited[nr][nc] = True
                        deq.append((nr,nc))
                        path[nr][nc].append((row,col))

                        if map_list[nr][nc] == 'X':
                            memo_X.append((nr,nc))
                        
                        if map_list[nr][nc] == 'E':
                            path[nr][nc].append((row,col))
                            visited[nr][nc] = True
                            r,c = nr,nc
                            break
    
    while len(memo_X) > 0:
        r1,c1 = r,c
        path
        
                

N,M = map(int,input().split())

map_list = [list(input()) for _ in range(M)]
visited = [[False for _ in range(N)] for _ in range(M)]
path = [[[] for _ in range(N)] for _ in range(M)]
memo_X = []

count_X = 0
for row in range(M):
    for col in range(N):
        if map_list[row][col] == 'X':
            count_X += 1


for row in range(M):
    for col in range(N):
        if visited[row][col] == False:
            if map_list[row][col] == 'S':
                bfs(row,col)
print(path)
print(memo_X)
print(r,c)