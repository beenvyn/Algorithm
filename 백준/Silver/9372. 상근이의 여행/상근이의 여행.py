import sys

input = sys.stdin.readline

t = int(input().strip())
answer = []

for _ in range(t):
    n, m = map(int, input().rstrip().split())
    
    visited = [False] * (n + 1)
    graph = [[] for _ in range(n+1)]


    for _ in range(m):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)
    
    cnt = 0
    
    def dfs(c):
        global cnt
        visited[c] = True

        for neigh in graph[c]:
            if not visited[neigh]:
                cnt += 1
                dfs(neigh)

    dfs(1)
    answer.append(cnt)

for a in answer:
    print(a)