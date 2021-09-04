import collections

def bfs2(row,col):
    deq = collections.deque()
    deq.append((row,col))
    visited2[row][col] = True
    ice_count = 1

    dr = [0,0,-1,1]
    dc = [-1,1,0,0]

    while len(deq) > 0:
        row,col = deq.popleft()

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]

            if 0 <= nr < map_count and  0 <= nc < map_count:
                if visited2[nr][nc] == False:
                    if map_list[nr][nc] != 0:
                        deq.append((nr,nc))
                        visited2[nr][nc] = True
                        ice_count += 1
    
    return ice_count

#---------------------------------------------- bfs
N,Q = map(int,input().split())
map_count = 1
for _ in range(N):
    map_count *= 2
map_list = [list(map(int,input().split())) for _ in range(map_count)]

L = list(map(int,input().split()))
deq2 = collections.deque()

for i in L:
    deq2.append(i)

#----------------------------------------------

while len(deq2) > 0:
    x = deq2.popleft()

    rectangle = 1
    
    if x != 0:
        for _ in range(x):
            rectangle *= 2
    elif x == 0 :
        rectangle == 1

    total_ice = 0
    ice_map = [[0 for _ in range(map_count)] for _ in range(map_count)]


    for row in range(0,map_count,rectangle):
        for col in range(0,map_count,rectangle):
            for r in range(row,rectangle+row):
                for c in range(col,rectangle+col):
                    ice_map[row+c-col][row+col+rectangle-r-1] = map_list[r][c]
    
    dr = [0,0,-1,1]
    dc = [-1,1,0,0]
    all_cut = collections.deque()
    for row in range(map_count):
        for col in range(map_count):
            if ice_map[row][col] != 0:
                near_ice = 0
                for i in range(4):
                    nr = row + dr[i]
                    nc = col + dc[i]

                    if 0 <= nr < map_count and 0<= nc < map_count:
                        if ice_map[nr][nc] == 0:
                            near_ice += 1
                    else:
                        near_ice += 1
                
                if near_ice > 1:
                    all_cut.append((row,col))
    
    while len(all_cut) > 0 :
        row,col = all_cut.popleft()
        ice_map[row][col] -= 1

    map_list = [item[:] for item in ice_map]
    


ice_dong = 0
visited2 = [[False for _ in range(map_count)] for _ in range(map_count)]

for row in range(map_count):
    for col in range(map_count):
        if map_list[row][col] != 0:
            if visited2[row][col] == False:
                ice_k = bfs2(row,col)
                if ice_dong < ice_k:
                    ice_dong = ice_k

for row in range(map_count):
        for col in range(map_count):
            total_ice += map_list[row][col]


print(total_ice)
print(ice_dong)