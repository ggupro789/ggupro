import collections
import copy

def bfs(row,col,list):
    global map_list

    deq = collections.deque()
    deq.append((row,col))
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[row][col] = True

    dr = [0,0,-1,1]
    dc = [-1,1,0,0]

    while len(deq)>0:
        row,col = deq.popleft()

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]

            if 0 <= nr < N and 0 <= nc < M:
                if list[nr][nc] == 0:
                    if visited[nr][nc] == False:
                        deq.append((nr,nc))
                        visited[nr][nc] = True
                        list[nr][nc] = 2
    
    return 

def my_combination(start,target):
    global count
    global map_list

    count0 = 0
    if target == 3:
        #탈출
        map_list2 = copy.deepcopy(map_list)
        for row in range(N):
            for col in range(M):
                if map_list[row][col] == 2 :
                    bfs(row,col,map_list2)
                    
        for row in range(N):
            for col in range(M):
                if map_list2[row][col] == 0:
                    count0 += 1
        if count < count0:
            count = count0
        
        return
        
    for i in range(start,N*M): # 2 차원 배열 조합 할때 필수
        row = i // M
        col = i % M
        if map_list[row][col] == 0:
            map_list[row][col] = 1
            my_combination(i,target + 1)
            map_list[row][col] = 0

N,M = map(int,input().split())
map_list = [list(map(int,input().split())) for _ in range(N)]
count = 0

my_combination(0,0)

print(count)

