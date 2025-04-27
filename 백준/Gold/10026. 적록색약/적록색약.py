import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
ans1 = 0
ans2 = 0
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    visited[x][y] = True
    cur_color = graph[x][y]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if (0 <= nx < n) and (0 <= ny < n):
            #현재 좌표의 색상과 같으면 dfs로 넣어준다
            if not visited[nx][ny] and graph[nx][ny] == cur_color:
                dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            ans1 += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            ans2 += 1

print(ans1, ans2)