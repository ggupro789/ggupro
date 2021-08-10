import collections

def bfs(row,col):


R,C = map(int,input().split())

map_list = [[input().rstrip()] for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]

for row in range(R):
    for col in range(C):
        if map_list[row][col] != "#" and visited[row][col] == 0:
            
