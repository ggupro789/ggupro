from collections import deque

def bfs(row,col):                   # BFS
    deq = deque()
    deq.append((row,col))
    
    visited[row][col] = 1

    v_count = 0
    k_count = 0
    if map_list[row][col] == 'v':
        v_count += 1
    elif map_list[row][col] == 'k':
        k_count += 1

    dr = [0,0,-1,1]
    dc = [-1,1,0,0]

    while len(deq) > 0:
        row,col = deq.popleft()

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            
            if 0 <= nr < R and 0 <= nc < C:
                if map_list[nr][nc] != '#':
                    if visited[nr][nc] == 0:
                        if map_list[nr][nc] == 'v':
                            v_count += 1
                            visited[nr][nc] = 1
                            deq.append((nr,nc))

                        elif map_list[nr][nc] == 'k':
                            k_count += 1
                            visited[nr][nc] = 1
                            deq.append((nr,nc))

                        else:
                            visited[nr][nc] = 1 
                            deq.append((nr,nc))
    if k_count > v_count:
        return 0,k_count
    else:
        return v_count,0


R,C = map(int,input().split())

map_list = [list(input().rstrip()) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
v,k = 0,0

for row in range(R):
    for col in range(C):
        if map_list[row][col] != "#" and visited[row][col] == 0:
            v1,k1 = bfs(row,col)
            v += v1
            k += k1
print(k,v)