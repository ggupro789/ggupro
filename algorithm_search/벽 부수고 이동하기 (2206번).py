import collections


def bfs():
    deq = collections.deque()
    deq.append((0,0,1))
    visited = [[[0,0] for _ in range(M)] for _ in range(N)]    
    visited[0][0][1] = 1
    
    dr = [0,0,-1,1]
    dc = [-1,1,0,0]

    while len(deq)>0:
        row,col,wall= deq.popleft()

        if row == N-1 and col == M-1:
            print(visited)
            return visited[row][col][wall]

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            
            if 0 <= nr < N and 0 <= nc < M:
                if map_list[nr][nc] == 1 and wall == 1:
                    visited[nr][nc][0] = visited[row][col][1] + 1
                    deq.append((nr,nc,0))

                elif map_list[nr][nc] == 0 and visited[nr][nc][wall] == 0:
                    visited[nr][nc][wall] = visited[row][col][wall] + 1
                    deq.append((nr,nc,wall))
    return -1

         
N,M = map(int,input().split())
map_list = [list(map(int,input())) for _ in range(N)]
print(bfs())