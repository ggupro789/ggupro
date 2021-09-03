import collections

def bfs(row,col):
    deq = collections.deque()
    deq.append((row,col))
    visited[row][col] = True

    dr = [0,0,-1,1]
    dc = [-1,1,0,0]

    ice_count = 1

    while len(deq) > 0:
        
        row,col = deq.popleft()
        near_ice = 0

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]

            if 0 <= nr < map_count and 0 <= nc < map_count:
                if visited[nr][nc] == False:
                    if ice_map[nr][nc] != 0:
                        visited[nr][nc] = True
                        ice_count += 1
                        deq.append((nr,nc))

                    elif ice_map[nr][nc] == 0:
                        near_ice += 1
                        
                elif visited[nr][nc] == True:
                    if ice_map[nr][nc] == 0:
                        near_ice += 1
                
            elif nr < 0 or nr >= map_count or nc < 0 or nc >= nc:
                near_ice += 1
            
        if near_ice >= 2:
            ice_map[row][col] -= 1
        
    return ice_count

N,Q = map(int,input().split())
map_count = 1
for _ in range(N):
    map_count *= 2
map_list = [list(map(int,input().split())) for _ in range(map_count)]

L = list(map(int,input().split()))


while len(L) > 0:
    x = L[0]
    L.remove(x)
    visited = [[False for _ in range(map_count)] for _ in range(map_count)]

    ice_dong = 0
    rectangle = 1

    for _ in range(x):
        rectangle *= 2
    print(map_list)
    total_ice = 0
    ice_map = [[0 for _ in range(map_count)] for _ in range(map_count)]
   
    for row in range(0,map_count,rectangle):
        for col in range(0,map_count,rectangle):
            for r in range(row,rectangle+row):
                for c in range(col,rectangle+col):
                    ice_map[c-col+row][row+col+rectangle-r-1] = map_list[r][c]
    print(ice_map)
    map_list = ice_map

    for row in range(map_count):
        for col in range(map_count):
            if ice_map[row][col] != 0:
                if visited[row][col] == False:
                    ice_k = bfs(row,col)

            if ice_dong < ice_k:
                ice_dong = ice_k
    
    for row in range(map_count):
        for col in range(map_count):
            total_ice += ice_map[row][col]


print(total_ice)
print(ice_k)