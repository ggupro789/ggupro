import collections

def bfs(row,col,list:list):
    deq = collections.deque()
    deq.append((row,col))

    game_map = [item[:] for item in list]
    dr = [0,0,-1,1]
    dc = [-1,1,0,0]

    while list.count(1)>0:
        for c in game_map[N]:

            for i in range(4):
                nr = row + dr[i]
                nc = row + dc[i]

                if c == 2:
                    if N-D <= nr < N and 0 <= nc <= M:
                        if game_map[nr][nc] == 1:
                            if 
                             


def my_combination(list, k, r,target):
    if len(target) == r:
        row_list = [0 for _ in range(M)]
        game_map = [item[:] for item in map_list]
        for i in target:
            row_list[i] = 2

        game_map.append(row_list)
        bfs()
        
        return

    if k > M-1: #  k의 역활 이해
        return

    my_combination(list,k+1,r,target)
    my_combination(list,k+1,r,target+[list[k]])


N,M,D = map(int,input().split())

map_list = [list(map(int,input().split())) for _ in range(N)]
my_combination([i for i in range(M)],0,3,[])
