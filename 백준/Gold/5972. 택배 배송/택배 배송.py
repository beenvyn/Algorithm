import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

costs = [float('inf')] * (N + 1)
costs[1] = 0
pq = [(0, 1)]

while pq:
    cur_cost, u = heapq.heappop(pq)

    if cur_cost > costs[u]:
        continue
    
    for v, c in graph[u]:
        next_cost = cur_cost + c
        if next_cost < costs[v]:
            costs[v] = next_cost
            heapq.heappush(pq, (next_cost, v))

print(costs[N])