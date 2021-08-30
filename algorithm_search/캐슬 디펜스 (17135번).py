import collections

def kill(target:list,game_map:list):
    kill_point = 0
    hmm = 0
    while True:
        game_set = 0

        for row in range(N):
            for col in range(M):
                if game_map[row][col] == 1:
                    game_set += 1
        
        if game_set == 0:
            break

        for i in target:
            count = 0
            cut = 100000
            r,c = 0,0
            for row in range(N):
                for col in range(M):   
                    if game_map[row][col] == 1 or game_map[row][col] == 3:
                        if D+hmm >= (abs(N-row) + abs(i-col)):
                            gimoring = (abs(N-row) + abs(i-col))
                            if cut > gimoring:
                                cut = gimoring
                                r,c = row,col

                            if cut == gimoring:
                                if c > col:
                                    r,c = row,col
            if cut != 100000:
                game_map[r][c] = 3
            

                            
        for row in range(N):
            for col in range(M):
                if game_map[row][col] == 3:
                    kill_point += 1
                    game_map[row][col] = 0
        
        game_map[N-1-hmm] = [0 for _ in range(M)]

        hmm += 1

    
    return kill_point


def my_combination(list, k, r,target):
    global count

    if len(target) == r:
        # row_list = [0 for _ in range(M)]

        game_map = [item[:] for item in map_list]
        countre = 0

        
        countre = kill(target,game_map)

        if count < countre:
            count = countre
           
        return

    if k > M-1: #  k의 역활 이해
        return

    my_combination(list,k+1,r,target)
    my_combination(list,k+1,r,target+[list[k]])


N,M,D = map(int,input().split())

map_list = [list(map(int,input().split())) for _ in range(N)]
count = 0
my_combination([i for i in range(M)],0,3,[])


print(count)