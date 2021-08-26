import collections

def bfs(N,K):
    deq = collections.deque()
    deq.append((N))


    while len(deq)>0:
        flow = deq.popleft()

        if flow == K:    # 탈출 조건
            print(visited[flow])
            answer = []    # path 경로 받기위한 리스트

            while flow != N:   
                answer.append(flow)  # flow == K 부터 N까지 
                flow = path[flow]    # path[]의 값들은 이전 경로의 값들을 가져온다고 보면 된다.
            
            answer.append(N)        
            answer.reverse()        # 받아온 값들이 K부터 니까 역순으로 바꿔준다.
            print(' '.join(map(str,answer)))

            return

        for next in (flow+1,flow-1,flow*2):   ## ****** visited의 값들은 한 마디로 트리의 높이로 생각하고 path는 이전 경로를 저장한다.
            if 0 <= next < 100001 and visited[next] == 0:
                visited[next] = visited[flow] + 1
                path[next] = flow
                deq.append(next)    # 위의 입력된 값들을 데크로 저장 때리면 자연스럽게 너비 탐색 가능

N,K = map(int,input().split())
visited = [0 for _ in range(100001)]
path = [0 for _ in range(100001)]
bfs(N,K)
