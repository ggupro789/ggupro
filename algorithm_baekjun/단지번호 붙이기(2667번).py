#단지번호 붙이기

import collections

def bfs(row,col):
    deq = collections.deque()
    deq.append((row,col))

    visited[row][col] = 1

    dr = [0,0,-1,1]
    dc = [-1,1,0,0]
    count_n = 1

    while len(deq) > 0:
        row, col = deq.popleft()

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                if map_list[nr][nc] == 1:
                    if visited[nr][nc] == 0:
                        
                        visited[nr][nc] = 1
                        deq.append((nr,nc))
                        count_n += 1
    
    return count_n



N = int(input())

map_list = [[0 for _ in range(N)] for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
result_list = []
count = 0

for line in range(N):
    N_line = list(map(int,input()))
    map_list[line] = N_line

for row in range(N):
    for col in range(N):
        if map_list[row][col] == 1:
            if visited[row][col] == 0:
                result_list.append(bfs(row,col))
                count += 1

print(count)
result_list = sorted(result_list)
for i in range(len(result_list)):
    print(result_list[i])
