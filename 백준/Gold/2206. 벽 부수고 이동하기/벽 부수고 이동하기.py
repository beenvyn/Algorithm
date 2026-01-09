import sys
from collections import deque
input = sys.stdin.readline

rows, cols = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(rows)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[[0, 0] for _ in range(cols)] for _ in range(rows)]
que = deque([(0, 0, 1, 1)])
visited[0][0][0] = 1

while que:
    r, c, dist, flag = que.popleft()
    if r == rows - 1 and c == cols - 1:
        print(dist)
        break

    for d in dirs:
        nr, nc = r + d[0], c + d[1]

        if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc][flag]:
            if grid[nr][nc] == '0': # 일반 이동
                que.append((nr, nc, dist + 1, flag))
                visited[nr][nc][flag] = 1
        
            if flag and grid[nr][nc] == '1': # 벽 부수기
                que.append((nr, nc, dist + 1, 0))
                visited[nr][nc][0] = 1 # 벽을 부순 후에는 flag=0이 됨.
else:
    print(-1)