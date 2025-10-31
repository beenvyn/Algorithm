import sys
from collections import deque

input = sys.stdin.readline

rows, cols = map(int, input().split())
grid = [list(map(int,input().split())) for _ in range(rows)]

dirs = [(0,-1), (0,1), (-1,0), (1,0)]
time = 0

def melt(): # 1년 후 빙산 상태
    new_grid = [row[:] for row in grid]
    que = deque([])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 0:
                que.append((r,c))

                while que:
                    r, c = que.popleft()

                    for d in dirs:
                        nr, nc = r + d[0], c + d[1]

                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                            if new_grid[r][c] > 0:
                                new_grid[r][c] -= 1
    
    return new_grid

def finished(arr):
    for row in arr:
        if any(row):
            return False
    return True

def count(r,c,visited):
    que = deque([(r,c)])
    visited[r][c] = True

    while que:
        r, c = que.popleft()

        for d in dirs:
            nr, nc = r + d[0], c + d[1]

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 0 and not visited[nr][nc]:
                visited[nr][nc] = True
                que.append((nr,nc))
                       
while not finished(grid):
    grid = melt()
    time += 1
    islands = 0

    visited = [[False] * cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 0 and not visited[r][c]:
                count(r,c,visited)
                islands += 1
    
    if islands >= 2:
        print(time)
        sys.exit(0)

print(0)
    
