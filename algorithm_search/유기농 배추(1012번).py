#유기농 배추 문제 (백준)
import collections

def bfs(row, col):   # 너비 탐색 함수
    deq = collections.deque() # 큐로 사용할 데크
    deq.append((row,col)) 
    
    visited[row][col] = 1

    dc = [-1, 1, 0, 0]
    dr = [0, 0, -1, 1]

    while len(deq) > 0 :  #데크 크기만큼 반복
        row, col = deq.popleft() 

        for i in range(4): # 시작점부터 상하좌우 조사

            nc = col + dc[i]
            nr = row + dr[i]

            if 0 <= nc < M and 0 <= nr < N:     # map_list 안 벗어나도록
                if map_list[nr][nc] == 1:       # 
                    if visited[nr][nc] == 0:

                        visited[nr][nc] = 1
                        deq.append((nr,nc))


test_case = int(input())

for _ in range(test_case):
    M,N,K = map(int,input().split())
    map_list = [[0 for _ in range(M)] for _ in range(N)]

    count = 0

    visited = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        col, row = map(int,input().split())

        map_list[row][col] = 1
    
    for col in range(M):
        for row in range(N):
           if map_list[row][col] == 1:
                if visited[row][col] == 0:
                    bfs(row,col)
                    count +=1

    print(count)