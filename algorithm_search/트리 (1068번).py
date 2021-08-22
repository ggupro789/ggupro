def dfs(node):
  if graph[node] == -2:
    return 0
  if graph[node] == -1:
    return 1
  
  if graph[node] != -1 or graph[node] != -2:
    count = dfs(graph[node])
    
  return count

N = int(input())

graph = list(map(int,input().split()))
del_node = int(input())
fuc = [i for i in range (N)]
leaf = []
count = 0

graph[del_node] = -2

for i in fuc:
  if i not in graph:
    leaf.append(i)


for node in leaf:
  count += dfs(node)

print(count)