from collections import deque

def bfs(B):
    deq = deque()
    deq.append(B)
    visited = [0 for _ in range(N+1)]
    visited[B] = 1

    count = 0

    while len(deq) > 0:
        B1 = deq.popleft()
        
        for j in map_list[B1]:
            if visited[j] == 0 :
                deq.append(j)
                visited[j] = 1
                count += 1

    return count


N,M = map(int,input().split())
map_list = [[] for _ in range(N+1)]
maxi = 0
now = 0
result = []

for _ in range(M):
    a,b = map(int,input().split())
    map_list[b].append(a)

for computer in range(1,N+1):
    now = bfs(computer)
    if now > maxi:
        maxi = now
        result = [computer]
    elif now == maxi:
        result.append(computer)

for best in range(len(result)):
    if best != len(result):
        print("{0}".format(result[best]),end = " ")
    else:
        print("{0}".format(result[best]))