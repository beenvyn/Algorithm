def solution(n, computers):
    answer = 0
    
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                graph[i].append(j)
                graph[j].append(i)
    
    visited = [False] * n
    
    def dfs(node):
        visited[node] = True
        
        for v in graph[node]:
            if not visited[v]:
                dfs(v)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    
    return answer