def dfs(start_v,visited_d : list): # DFS
    visited_d.append(start_v)

    for node in sorted(graph[start_v]):
        if node not in visited_d:
            visited_d = dfs(node,visited_d)
    
    return visited_d