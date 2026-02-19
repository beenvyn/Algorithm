from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    distances = [-1] * (n + 1)
    distances[1] = 0
    que = deque([1])
    
    while que:
        node = que.popleft()
        
        for v in graph[node]:
            if distances[v] == -1:
                distances[v] = distances[node] + 1
                que.append(v)
    
    for d in distances:
        if d == max(distances):
            answer += 1

    return answer