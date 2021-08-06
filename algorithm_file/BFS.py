from collections import deque

def bfs(start_V):                   # BFS
    deq = deque()
    deq.append(start_V)
    
    visited_b.append(start_V)
    
    dr = [0,0,-1,1]
    dc = [-1,1,0,0]

    while len(deq) > 0:
        node = deq.popleft()
        
        for n in sorted(graph[node]):
            if n not in visited_b:
                visited_b.append(n)
                deq.append(n)
    
    return visited_b