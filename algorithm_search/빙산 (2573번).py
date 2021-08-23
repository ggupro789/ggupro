def dfsarea(row,col):
  stack = []
  stack.append((row,col))
  visitedArea[row][col] = True
  while len(stack)>0:
    row,col = stack.pop()

    for i in range(4):
      nr = row + dr[i]
      nc = col + dc[i]

      if 0 <= nr < N and 0 <= nc < M:
        if visitedArea[nr][nc] == False:
          if map_list[nr][nc] != 0:
            visitedArea[nr][nc] = True
            stack.append((nr,nc))
  
  return visitedArea

def dfs0(row,col):
  stack = []
  stack.append((row,col))
  visited0[row][col] = True
  while len(stack)>0:
    row,col = stack.pop()

    for i in range(4):
      nr = row + dr[i]
      nc = col + dc[i]

      if 0 <= nr < N and 0 <= nc < M:
        if visited0[nr][nc] == False:
          if map_list[nr][nc] != 0:
            map_list[nr][nc] -= 1
            if map_list[nr][nc] == 0:
              visited0[nr][nc] = True
              
          elif map_list[nr][nc] == 0:
            visited0[nr][nc] = True
            stack.append((nr,nc))
  
  return visited0

N,M = map(int,input().split())

map_list = [list(map(int,input().split())) for _ in range(N)]

dr = [0,0,-1,1]
dc = [-1,1,0,0]
count = 0

while True:
  visited0 = [[False for _ in range(M)] for _ in range(N) ]
  visitedArea = [[False for _ in range(M)] for _ in range(N) ]
  countarea = 0

  for row in range(N):
    for col in range(M):
      if map_list[row][col] != 0 and visitedArea[row][col] == False:
        dfsarea(row,col)
        countarea += 1
  
  if countarea == 0:
    count = 0
    break

  if countarea >= 2:
     break

  else:
    for row in range(N):
      for col in range(M):
        if map_list[row][col] == 0 and visited0[row][col] == False:
          dfs0(row,col)
  
  count += 1



print(count)