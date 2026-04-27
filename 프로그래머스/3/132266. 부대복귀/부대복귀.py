from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    
    graph = [[] for _ in range(n + 1)]
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    # 목적지가 하나로 고정돼있으니까 목적지 → 모든 노드 거리를 한 번만 구하면 됨
    dist = [-1] * (n + 1)
    dist[destination] = 0
    
    que = deque([destination])
    
    while que:
        node = que.popleft()
        
        for nxt in graph[node]:
            if dist[nxt] == -1:
                dist[nxt] = dist[node] + 1
                que.append(nxt)
    
    for s in sources:
        answer.append(dist[s])
    
    return answer