import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e, p = map(int, input().split())
    graph[s].append([e, p])

A, B = map(int, input().split())

prices = [float('inf')] * (N + 1)
prices[A] = 0
pq = [(0, A)]

while pq:
    cur_price, u = heapq.heappop(pq)

    if prices[u] < cur_price:
        continue

    for v, p in graph[u]:
        next_price = cur_price + p

        if next_price < prices[v]:
            prices[v] = next_price
            heapq.heappush(pq, (next_price, v))

print(prices[B])