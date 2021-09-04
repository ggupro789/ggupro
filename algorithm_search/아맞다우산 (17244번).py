import collections

def bfs(row,col):
    deq = collections.deque()
    deq.append(row,col)

    dr = [0,0,-1,1]
    dc = [-1,1,0,0]

    

N,M = map(int,input().split())

map_list = [list(input()) for _ in range(M)]
visited = [[False for _ in range(N)] for _ in range(M)]

for row in range(N):
    for col in range(M):
        if map_list[row][col] == 'S':
            bfs(row,col)