from collections import deque

def bfs(row,col):                   # BFS
    deq = deque()
    deq.append((row,col))
    
    visited[row][col] = 1

    dr = [0,0,-1,1,-1,-1,1,1]
    dc = [-1,1,0,0,1,-1,1,-1]

    while len(deq) > 0:
        row,col = deq.popleft()

        for i in range(8):
            nr = row + dr[i]
            nc = col + dc[i]

            if 0 <= nr < h and 0 <= nc < w:
                if map_list[nr][nc] == 1:
                    if visited[nr][nc] == 0:
                        visited[nr][nc] = 1
                        deq.append((nr,nc))
        

while True:
    count = 0
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    
    map_list = [list(map(int,input().split())) for _ in range(h)]
    visited = [[0 for _ in range(w)] for _ in range(h)]
    

    for row in range(h):
        for col in range(w):
            if map_list[row][col] == 1:
                if visited[row][col] == 0:
                    bfs(row,col)
                    count += 1
    
    print(count)