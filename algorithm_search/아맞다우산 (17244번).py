import collections

def bfs(row,col,x_list):

    deq = collections.deque()
    deq.append((row,col))
    visited = [[False for _ in range(N)] for _ in range(M)]
    visited[row][col] = True
    rr,cc = row,col
    dr = [0,0,-1,1]
    dc = [-1,1,0,0]

    count = 0
    index = 0

    while index < len(x_list):
        row,col = deq.popleft()
        
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]

            if 0 <= nr < M and 0 <= nc < N:
                if map_list[nr][nc] != '#':
                    if visited[nr][nc] == False:
                        visited[nr][nc] = True
                        deq.append((nr,nc))
                        path[nr][nc].append((row,col))

                        if map_list[nr][nc] == x_list[index]:
                            deq.clear()
                            deq.append((nr,nc))
                            visited = [[False for _ in range(N)] for _ in range(M)]
                            r,c = x_list[index]
                            index += 1
                            
                            while a != rr and b != cc:
                                a,b = path[r][c]
                                r,c = a,b
                                count += 1
                            
                            rr,cc = nr,nc
                            continue
    print(count)




#------------------------------------------
def my_permutations(list,r,target):
    #탈출조건
    if len(target) == r:
        # 결과를 수행하라
        bfs(s_row,s_col,target)
        return

    for i in range(len(list)):
        if visited_x[i] == False:
            visited_x[i] = True
            my_permutations(list,r,target+[list[i]])
            visited_x[i] = False # false로 다시 바꿔줘야 한다.


#--------------------------------------------------
        
                

N,M = map(int,input().split())

map_list = [list(input()) for _ in range(M)]
path = [[[] for _ in range(N)] for _ in range(M)]

memo_X = []

for row in range(M):
    for col in range(N):
        if map_list[row][col] == 'S':
            s_row,s_col = row,col
        if map_list[row][col] == 'X':
            memo_X.append((row,col))
        if map_list[row][col] == 'E':
            e_row,e_col = row,col
# print(path)
visited_x = [False for _ in range(len(memo_X))]

my_permutations(memo_X,len(memo_X),[])