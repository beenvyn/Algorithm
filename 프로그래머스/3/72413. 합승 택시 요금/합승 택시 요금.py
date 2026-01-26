import heapq

def solution(n, s, a, b, fares):
    answer = float('inf')
    graph = [[] for _ in range(n + 1)]
    
    for x, y, d in fares:
        graph[x].append([y, d])
        graph[y].append([x, d])
        
    def dijkstra(start):
        dist = [float('inf')] * (n + 1)
        dist[start] = 0
        pq = [(0, start)]
        
        while pq:
            cur_dist, u = heapq.heappop(pq)
            
            if cur_dist > dist[u]:
                continue
            
            for v, d in graph[u]:
                next_dist = cur_dist + d
                if next_dist < dist[v]:
                    dist[v] = next_dist
                    heapq.heappush(pq, (next_dist, v))
        return dist
    
    from_s = dijkstra(s)
    from_a = dijkstra(a)
    from_b = dijkstra(b)
            
    for i in range(1, n + 1): # 1부터 n까지 합승하는 경우
        dist = from_s[i] + from_a[i] + from_b[i]
        answer = min(answer, dist)
    
    # 합승 안하는 경우
    answer = min(answer, from_s[a] + from_s[b])
    
    return answer