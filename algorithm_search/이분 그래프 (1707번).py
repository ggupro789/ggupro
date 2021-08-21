import sys
sys.setrecursionlimit(10000)

def dfs(node,visited):
    visited[node] = 1
    
    if node < V:
        if visited[graph[node]] == 0:
            dfs(graph[node],visited)

K  = int(input())

for _ in range(K):
    V,E = map(int,input().split())
    graph = [0 for _ in range(V)]
    visited = [0 for _ in range(V)]
    count = 0

    for _ in range(E):
        V1,E1 = map(int,input().split())
        graph[V1] = E1
    
    
    if count == 2:
        print("YES")
    else:
        print("NO")
