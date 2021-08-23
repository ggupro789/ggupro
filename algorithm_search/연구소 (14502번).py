# for item in itertools.permutations(temp_list,4):
#     print(item)
def bfs():
    print

# def my_combination(list, k, r, target):
#     if len(target) == r:
#         #탈출
#         print(target)
#         return

#     if k >= len(list): #  k의 역활 이해
#         return

    
#     my_combination(list,k+1,r,target)
#     my_combination(list,k+1,r,target+[list[k]])

N,M = map(int,input().split())
map_list = [list(map(int,input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

