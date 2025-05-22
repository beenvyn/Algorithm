import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())

graph = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([1])
parent[1] = 0

while q:
    current = q.popleft()

    for neigh in graph[current]:
        if not parent[neigh]:
            parent[neigh] = current
            q.append(neigh)

for i in range(2, n + 1):
    print(parent[i])
