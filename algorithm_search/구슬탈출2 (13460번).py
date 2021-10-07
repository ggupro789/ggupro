from typing import Collection
import collections

def bfs():
    global count
    deq = collections.deque()
    deq.append(row_R,col_R,row_B,col_B)
    

    dr = [0,0,-1,1]
    dc = [-1,1,0,0]

    while len(deq) > 0:
        rowR,colR,rowB,colB = deq.popleft()
            
        for i in range(4):
            nrR = rowR + dr[i]
            ncR = colR + dc[i]
            nrB = rowB + dr[i]
            ncB = colB + dc[i]
            
            if 0 < nrR < N and 0 < ncR < M:
                if map_list[nrR][ncR] != '#':
                    if visited[nrR][ncR] == False:
                        while map_list[nrR][ncR] != '#':
                            if map_list[nrR][ncR] == 'O':
                                return
                            if map_list[nrR][ncR] == 'B':
                                break
                            nrR = nrR + dr[i]
                            ncR = ncR + dc[i]
                            visited[nrR][ncR] = True
                            
                        # deq.append((nrR-dr[i],ncR-dc[i]))

# -------------------------------------
N,M = map(int,input().split())
map_list = [list(input()) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
count = 0
row_R = 0,col_R = 0, row_B = 0, col_B = 0
for row in range(N):
    for col in range(M):
        if map_list[row][col] == 'R':
            row_R = row,col_R = col
        if map_list[row][col] == 'B':
            row_B = row,col_B = col

bfs()
print(count)


#--------------------------------------
# deq 에 한번에 빨간 파란 공을 다 넣는다.
# 움직이는 함수를 따로 만들어서 벽 부딪칠 때, 서로 만날 때, 먼저 공이 들어갈 때. 고려 해 준다.
# 포기