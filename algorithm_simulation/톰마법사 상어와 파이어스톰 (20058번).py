N,Q = map(int,input().split())
map_count = 1
for i in range(N):
    map_count *= 2
map_list = [list(map(int,input().split())) for _ in range(map_count)]
L = list(map(int,input().split()))

