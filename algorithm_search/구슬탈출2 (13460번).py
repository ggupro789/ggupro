from typing import Collection

import collections

def bfs():
    deqR = collections.deque()
    deqB = collections.deque()

    deqR.append(R_rowcol)
    deqB.append(B_rowcol)

    dr = [0,0,-1,1]
    dc = [-1,1,0,0]

    while len(deqR) > 0:
        rowR,colR = deqR.popleft()
        rowB,colB = deqB.popleft()

        for i in range(4):
            nrR = rowR + dr[i]
            ncR = colR + dc[i]

            nrB = rowB + dr[i]
            ncB = colB + dc[i]

            if 0 < nrR < N and 0 < ncR < M:
                if 



# -------------------------------------
N,M = map(int,input().split())
map_list = [list(input()) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

for row in range(N):
    for col in range(M):
        if map_list[row][col] == 'R':
            R_rowcol = (row,col)
        if map_list[row][col] == 'B':
            B_rowcol = (row,col)

bfs()
