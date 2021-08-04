# 토마토
import collections

def bfs(tomato1):
    # deq = collections.deque()

    # for first1 in range(len(tomato1)):
    #     deq.append((tomato1[first1]))
    #     visited[tomato1[first1][0]][tomato1[first1][1]] = 1

    # count = 0

    # dr = [0,0,-1,1]
    # dc = [-1,1,0,0]

    # while len(deq) > 0:
    #     list = deq.popleft()

    #     for _ in range(len(deq)):
    #         list = deq.popleft()
    #         print(row,col)
    #         for i in range(4):
    #             nr = row + dr[i]
    #             nc = col + dc[i]

    #             if 0 <= nr < N and 0<= nc < M:
    #                 if visited[nr][nc] == 0:
    #                     visited[nr][nc] = 1
    #                     deq.append((nr,nc))
        
        

    for i in range(N):
        if 0 in map_list[i]:
            return -1
        else:
            return count

M,N = map(int,input().split())

map_list = [list(map(int,input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
tomato1 = []

for row in range(N):
    for col in range(M):
        if map_list[row][col] == 1:
            tomato1.append([row,col])

result = bfs(tomato1)
print(result)



