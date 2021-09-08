import collections

def bfs(row,col,x_list):
    deq = collections.deque()
    deq.append((row,col))
    visited = [[False for _ in range(N)] for _ in range(M)]
    path = [[[] for _ in range(N)] for _ in range(M)]
    index = 0
    count = 0

    s_r,s_c = row,col

    dr = [0,0,-1,1]
    dc = [-1,1,0,0]

    while len(deq) > 0:
        row,col = deq.popleft()

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]

            if 0 <= nr < M and 0 <= nc < N:
                if visited[nr][nc] == False:
                    if map_list[nr][nc] != '#':
                        visited[nr][nc] = True
                        deq.append((nr,nc))
                        path[nr][nc] = row,col

                        if index != len(x_list):
                            if nr == x_list[index][0] and nc == x_list[index][1]:
                                a,b = 0, 0
                                deq.clear()
                                deq.append((nr,nc))
                                
                                while a != s_r or b != s_c:
                                    a,b = path[nr][nc]
                                    nr,nc = a,b
                                    count += 1

                                

                                index += 1
                                s_r,s_c = x_list[index-1][0],x_list[index-1][1] 
                                visited = [[False for _ in range(N)] for _ in range(M)]
                            
                                break
                        

                        elif index == len(x_list):
                            if nr == e_row and nc == e_col:
                                a,b = 0,0
                                while a != x_list[-1][0] or b != x_list[-1][1]:
                                    a,b = path[nr][nc]
                                    nr,nc = a,b
                                    count += 1
    
    return count


#------------------------------------------
def my_permutations(list,r,target):
    global count1
    #탈출조건
    if len(target) == r:
        # 결과를 수행하라
        
        count_x = bfs(s_row,s_col,target)
        if count1 > count_x:
            count1 = count_x
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
count1 = 100000

my_permutations(memo_X,len(memo_X),[])
print(count1)