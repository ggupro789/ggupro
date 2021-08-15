#DFS와 BFS
import collections
def dfs(start_v,visited_d : list): # DFS
    visited_d.append(start_v)

    for node in sorted(graph[start_v]):
        if node not in visited_d:
            visited_d = dfs(node,visited_d)
    
    return visited_d

def bfs(start_V):                   # BFS
    deq = collections.deque()
    deq.append(start_V)
    
    visited_b.append(start_V)

    while len(deq) > 0:
        node = deq.popleft()
        
        for n in sorted(graph[node]):
            if n not in visited_b:
                visited_b.append(n)
                deq.append(n)
    
    return visited_b


N, M, V = map(int,input().split())

graph = [[] for _ in range(N+1)]

visited_d = []
visited_b = []

for _ in range(M):
    N1,N2 = map(int,input().split())
    graph[N1].append(N2)
    graph[N2].append(N1)

# ---- 출력
result_d = dfs(V,visited_d)
result_b = bfs(V)

for i in range(len(result_d)):  
    if i < len(result_d)-1:
        print("{0}".format(result_d[i]),end=" ")
    else:
        print("{0}".format(result_d[i]))

for i in range(len(result_b)):
    if i < len(result_b)-1:
        print("{0}".format(result_b[i]),end=" ")
    else:
        print("{0}".format(result_b[i]))

