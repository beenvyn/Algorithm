import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input().rstrip())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

dist = [float('inf')] * (V + 1)
dist[start] = 0

pq = [(0, start)]

while pq:
    cur_dist, u = heapq.heappop(pq)

    if cur_dist > dist[u]:
        continue

    for v, w in graph[u]:
        next_dist = w + cur_dist

        if next_dist < dist[v]:
            dist[v] = next_dist
            heapq.heappush(pq, (next_dist, v))

for d in dist[1:]:
    print(d if d != float('inf') else 'INF')