import sys
sys.setrecursionlimit(10000)

def dfs(row,col,color):
    global visited
        
    visited[row][col] = 1
    dr = [0,0,-1,1]
    dc = [-1,1,0,0]


    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]

        if 0 <= nr < N and 0 <= nc < N:
            if map_list[nr][nc] == color:
                if visited[nr][nc] == 0:
                    dfs(nr,nc,color)
    

N = int(input())

map_list = [list(map(str, input())) for _ in range(N)]

visited = [[0 for _ in range(N)] for _ in range(N)]

countno = 0
countyes = 0

for row in range(N):
    for col in range(N):
        if visited[row][col] == 0:
            dfs(row,col,map_list[row][col])
            countno += 1

for row in range(N):
    for col in range(N):
        if map_list[row][col] == 'G':
            map_list[row][col] = 'R'

visited = [[0 for _ in range(N)] for _ in range(N)]

for row in range(N):
    for col in range(N):
        if visited[row][col] == 0:
            dfs(row,col,map_list[row][col])
            countyes += 1

print(countno,end= ' ')
print(countyes)
