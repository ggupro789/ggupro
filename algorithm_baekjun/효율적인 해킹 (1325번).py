from collections import deque

def bfs(B):
    deq = deque()
    deq.append(B)

    while len(deq) > 0:
        B1 = deq.popleft()

        for row in range(M):
            if map_list[row][1] == map_list[B1][0] and visited[row] == 0 :
                deq.append()

        

N,M = map(int,input().split())
map_list = [list(map(int,input().split())) for _ in range(M)]
count = []
visited = [0 for _ in range(M)] # 행렬의 [1] 부분만 체크
