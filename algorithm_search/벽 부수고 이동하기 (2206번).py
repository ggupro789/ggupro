# import collections


# def bfs(row,col):
#     global count_short
#     count_1 = 0
#     deq = collections.deque()
#     deq.append((row,col,count_1))
#     visited = [[[0,0] for _ in range(M)] for _ in range(N)]    
    
#     dr = [0,0,-1,1]
#     dc = [-1,1,0,0]

#     while len(deq)>0:
#         row,col,count_1,visited = deq.popleft()

#         if row == N-1 and col == M-1:
#             count_in = 0
#             ans = []
#             while True:
#                 ans = visited[row][col]
#                 count_in += 1
#                 if ans == [0,1] or ans == [1,0]:
#                     return count_in + 2
#                 row = ans[0]
#                 col = ans[1]
    
#         for i in range(4):
#             nr = row + dr[i]
#             nc = col + dc[i]
            
#             if 0 <= nr < N and 0 <= nc < M:
#                 if map_list[nr][nc] == 1:
#                     count_1 += 1
#                     if count_1 == 1:
#                         if visited[nr][nc] == [0,0] :
#                             visited[nr][nc] = [row,col]
#                             deq.append((nr,nc,count_1))
                    
#                     count_1 -= 1

#                 elif map_list[nr][nc] == 0:
#                     if visited[nr][nc] == [0,0]:
#                         visited[nr][nc] = [row,col]
#                         deq.append((nr,nc,count_1))
                        
#     return -1

         
# N,M = map(int,input().split())
# map_list = [list(map(int,input())) for _ in range(N)]
# count = float('inf')
# count_short = 0

# count_short = bfs(0,0)
# if count > count_short and count_short != -1:
#     count = count_short
# elif count_short == -1:
#     count = count_short
# print(count)
