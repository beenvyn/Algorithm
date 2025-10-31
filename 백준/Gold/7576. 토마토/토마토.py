import sys
from collections import deque

input = sys.stdin.readline

cols, rows = map(int,input().split())
grid = [list(map(int, input().split())) for _ in range(rows)]

dirs = [(0,-1), (0,1), (-1,0), (1,0)]
dists = [[-1] * cols for _ in range(rows)]
starts = []

def bfs():
    que = deque([])
    for s in starts:
        que.append(s)
    
    while que:
        r, c, dist = que.popleft()
        dists[r][c] = dist

        for d in dirs:
            nr, nc = r + d[0], c + d[1]

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                grid[nr][nc] = 1
                que.append((nr,nc,dist+1))
    
    answer = 0
    for row in dists:
        answer = max(answer,max(row))
    
    return answer

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 1:
            starts.append((i,j,0))

ans = bfs()
for row in grid:
    if 0 in row:
        print(-1)
        exit(0)

print(ans)
