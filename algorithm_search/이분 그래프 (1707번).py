# import sys
# sys.setrecursionlimit(10000)

# def dfs(node,visited):
#     global graph

#     visited[node] = 1
#     k = graph[node]

#     if node < V:
#         if visited[k] == 0:
#             dfs(k,visited)

K  = int(input())

for _ in range(K):
    V,E = map(int,input().split())
    graph = [0 for _ in range(V+1)]
    # visited = [0 for _ in range(V+1)]
    count = 0
    result = []
    v_node =[]

    for i in range(0,V+1):
        result.append(i)

    for _ in range(E):
        V1,E1 = map(int,input().split())
        graph[V1] = E1

    
    for i in range(1,V+1):
        if graph[i] not in result:
            count += 1
    
    if count == 2:
        print("YES")
    else:
        print("NO")
    


    # for node in range(V):
    #     if visited[node] == 0:
    #         if graph[node] != 0:
    #             dfs(node,visited)
    #             count += 1

    
    
    # if count >= 2:
    #     print("NO")
    # else:
    #     print("YES")
