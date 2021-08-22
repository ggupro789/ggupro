import collections

def bfs(n):
    deq = collections.deque()
    deq.append((n,'RED'))
    visited[n] = [True,'Red']
    
    while deq:
        node, color = deq.popleft()
        for next_node in conj[node]:
            if visited[next_node][0] == False:
                if color =='Red':
                    visited[next_node]=[True,'BLACK']
                    deq.append((next_node,'Black'))
                elif color =='BLACK':
                    visited[next_node] = [True,'RED']
                    deq.append((next_node,'RED'))
            else:
                if color == visited[next_node][1]:
                    return 'NO'
    
    return 'YES'

T = int(input())

for test_case in range(1, T+1):
    V, E = map(int,input().split())
    conj = {i: [] for i in range(1,V+1)}
    result = 'YES'

    for _ in range(E):
        n1,n2 = map(int,input().split())
        conj[n1].append(n2)
        conj[n2].append(n1)

    visited =[[False,''] for _ in range(V+1)]
    for n in range(1,V+1):
        # VISITED 나중에
        if visited[n][0] == False:
            res = bfs(n)
                if res == 'NO':
                    result = 'NO'
                    break
    
    print(result)