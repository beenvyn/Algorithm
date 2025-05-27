def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(com):
        nonlocal visited
        visited[com] = True
        
        for i in range(n):
            if computers[com][i] == 1 and not visited[i]:
                dfs(i)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    
    return answer