import sys
import heapq
input = sys.stdin.readline

# 시작점에서 N까지의 최단 시간
def dijkstra(graph, start, N):
    time = [float('inf')] * (N + 1) # time[i]: start에서 i까지의 최단 시간
    time[start] = 0

    pq = [(0, start)]
    while pq:
        cur_time, u = heapq.heappop(pq)

        if cur_time > time[u]:
            continue

        for v, t in graph[u]:
            next_time = cur_time + t
            if next_time < time[v]:
                time[v] = next_time
                heapq.heappush(pq, (next_time, v))
    return time

N, M, X = map(int, input().split())
g = [[] for _ in range(N + 1)] # 원래 그래프
rg = [[] for _ in range(N + 1)] # 역방향 그래프

for _ in range(M):
    u, v, t = map(int, input().split())
    g[u].append([v, t])
    rg[v].append([u, t])

time_from_x = dijkstra(g, X, N)
time_to_x = dijkstra(rg, X, N)

answer = 0
for i in range(1, N + 1):
    answer = max(answer, time_to_x[i] + time_from_x[i])
            
print(answer)