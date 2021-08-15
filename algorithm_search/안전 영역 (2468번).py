# 안전 영역 2468번
import collections

def bfs(row,col,high): 
    deq = collections.deque()
    deq.append((row,col))
    visited[row][col] == 1

    dr = [0,0,-1,1]
    dc = [-1,1,0,0]

    while len(deq) > 0:

        row, col = deq.popleft()

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]

            if 0 <= nr < N and 0 <= nc < N and map_list[nr][nc] > high and visited[nr][nc] == 0:
                deq.append((nr,nc))
                visited[nr][nc] = 1



N = int(input())
map_list = [list(map(int,input().split())) for _ in range(N)]
result = []

for high in range(0,101):   # 높이 0~ 100 // 문제에선 1부터라 햇는데 ㅡ 맨밑에 아무지역도 물에 잠기지 않을수 잇다해서 0
    count = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]   # 높이마다 방문지역 초기화

    for row in range(N):
        for col in range(N):                              # 주어진 map_list 순회
            if map_list[row][col] > high and visited[row][col] == 0 :   # 높이 별로 안전영역 과 방문햇는지
                bfs(row,col,high)
                count += 1
    
    result.append(count)
                
print(max(result))