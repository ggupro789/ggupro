# 바이러스 2606번
import collections

def bfs(deq):
    dr = [0,0,-1,1]
    dc = [-1,1,0,0]

    while len(deq) > 0:
        row, col = deq.popleft()

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]

            if 0 <= nr < N and 0 <= nc < M and map_list[nr][nc] == 1:
                deq.append((nr,nc))
                map_list[nr][nc] = map_list[row][col] + 1


N,M = map(int,input().split())

map_list = [list(map(int,input())) for _ in range(N)]
deq = collections.deque()
deq.append((0,0))

bfs(deq)
print(map_list[N-1][M-1])

