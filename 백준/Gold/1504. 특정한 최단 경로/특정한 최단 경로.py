import sys
import heapq
input = sys.stdin.readline

def dijkstra(start, N):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0

    pq = [(0, start)]

    while pq:
        cur_dist, u = heapq.heappop(pq)

        if dist[u] < cur_dist:
            continue

        for v, d in graph[u]:
            next_dist = cur_dist + d

            if next_dist < dist[v]:
                dist[v] = next_dist
                heapq.heappush(pq, (next_dist, v))
    return dist

N, E = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().split())

d1 = dijkstra(1, N)
dv1 = dijkstra(v1, N)
dv2 = dijkstra(v2, N)

path1 = d1[v1] + dv1[v2] + dv2[N] # 1 -> v1 -> v2 -> N
path2 = d1[v2] + dv2[v1] + dv1[N] # 1 -> v2 -> v1 -> N

answer = min(path1, path2)
print(answer if answer < float('inf') else -1)