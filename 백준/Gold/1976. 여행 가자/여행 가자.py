import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
for i in range(N):
    info = list(map(int, input().split()))
    for j in range(N):
        if info[j]:
            graph[i + 1].append(j + 1)

route = list(map(int, input().split()))

# 첫 도시에서 갈 수 있는 모든 도시를 다 찍어보고, 여행 계획이 그 안에 다 포함되는지 확인하는 방식
visited = [False] * (N + 1)
def dfs(cur):
    visited[cur] = True

    for nxt in graph[cur]:
        if not visited[nxt]:
            dfs(nxt)

dfs(route[0])

for r in route:
    if not visited[r]:
        print('NO')
        break
else:
    print('YES')