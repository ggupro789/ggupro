import collections
import copy

def bfs(row,col):
    global count_short

    deq = collections.deque()
    deq.append((row,col))
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[row][col] = True

    dr = [0,0,-1,1]
    dc = [-1,1,0,0]
    count_in = 0

    while len(deq)>0:
        row,col = deq.popleft()

        if row == N-1 and col == M-1:
            return count_in

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]

            if 0 <= nr < N and 0 <= nc < M:
                if wall[nr][nc] == 0:
                    if visited[nr][nc] == False:
                        deq.append((nr,nc))
                        visited[nr][nc] = True
                        count_in += 1

    return -1

         



N,M = map(int,input().split())
map_list = [list(map(int,input())) for _ in range(N)]
wall = copy.deepcopy(map_list)
count = float('inf')
count_short = 0

for row in range(N):
    for col in range(M):
        if wall[row][col] == 1:
            wall[row][col] = 0
            count_short = bfs(0,0)
            wall[row][col] = 1

            if count > count_short and count_short != -1:
                count = count_short

print(count)
