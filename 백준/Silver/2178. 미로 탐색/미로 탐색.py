import sys
from collections import deque

input = sys.stdin.readline
n, m = list(map(int, input().split()))
graph = [list(map(int, input().rstrip())) for _ in range(n)]

answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque([[0,0]])

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < m):
            if graph[nx][ny] == 1:
                queue.append([nx, ny])
                graph[nx][ny] = graph[x][y] + 1

print(graph[n - 1][m - 1])