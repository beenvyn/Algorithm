import sys
from collections import deque
input = sys.stdin.readline

rows, cols, k = map(int, input().split())
graph = [input().rstrip() for _ in range(rows)]

dirs = [(0,1),(0,-1),(1,0),(-1,0)]
visited = [[[0]*(k+1) for _ in range(cols)] for _ in range(rows)]

que = deque([(0,0,1,k)])
visited[0][0][k] = 1

while que:
    r, c, dist, flag = que.popleft()

    if r == rows - 1 and c == cols - 1:
        print(dist)
        sys.exit(0)

    for d in dirs:
        nr, nc = r + d[0], c + d[1]

        if 0 <= nr < rows and 0 <= nc < cols:
            if flag > 0 and graph[nr][nc] == "1" and not visited[nr][nc][flag-1]:
                que.append((nr,nc,dist+1,flag-1))
                visited[nr][nc][flag-1] = 1
            elif graph[nr][nc] == "0" and not visited[nr][nc][flag]:
                que.append((nr,nc,dist+1,flag))
                visited[nr][nc][flag] = 1

print(-1)