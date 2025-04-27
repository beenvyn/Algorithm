def dfs(graph, v, visited):
    visited[v] = True

    for n in graph[v]:
        if not visited[n]:
            dfs(graph, n, visited)

n = int(input())
x = int(input())

graph = [[] for _ in range(n + 1)]
answer = 0

for i in range(x):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

dfs(graph, 1, visited)

for v in visited:
    if v:
        answer += 1

print(answer - 1)