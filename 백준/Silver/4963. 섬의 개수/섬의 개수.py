import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
answer = []

while True:
    c, r = map(int, input().split())
    if c == 0 and r == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(r)]
    visited = [[False] * c for _ in range(r)]
    
    def dfs(x, y):
        visited[x][y] = True
        for d in dirs:
            nx, ny = x + d[0], y + d[1]

            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)

    cnt = 0
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(i,j)
                cnt += 1
    answer.append(cnt)

print('\n'.join(map(str,answer)))