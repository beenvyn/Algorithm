import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

t = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(graph, i, j, n, m):
    graph[i][j] = 2

    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]

        if (0 <= nx < n) and (0 <= ny < m):
            if graph[nx][ny] == 1:
                dfs(graph, nx, ny, n, m)

for _ in range(t):
    m, n, k = list(map(int, input().rstrip().split()))
    
    graph = [[0] * m for _ in range(n)]
    answer = 0

    for _ in range(k):
        x, y = list(map(int, input().split()))
        graph[y][x] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(graph, i, j, n, m)
                answer += 1

    print(answer)