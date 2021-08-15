# 토마토
import collections

def bfs(deq:collections.deque):
    dr = [0,0,-1,1]
    dc = [-1,1,0,0]
    day = 0
    while len(deq) > 0:
        row, col = deq.popleft()

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]

            if 0 <= nr < N and 0 <= nc < M and map_list[nr][nc] == 0:
                deq.append((nr,nc))
                map_list[nr][nc] = map_list[row][col] + 1
    
    for r in map_list:
        for c in r:
            if c == 0:
                print(-1)
                exit()
    day = max(map(max,map_list))-1
    
    return day

M,N = map(int,input().split())

map_list = [list(map(int,input().split())) for _ in range(N)]
deq = collections.deque()

for row in range(N):
    for col in range(M):
        if map_list[row][col] == 1:
            deq.append((row,col))

print(bfs(deq))
