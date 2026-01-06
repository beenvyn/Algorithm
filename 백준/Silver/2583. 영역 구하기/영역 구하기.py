import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

rows, cols, K = map(int, input().split())
coords = [list(map(int, input().split())) for _ in range(K)]

grid = [[0] * cols for _ in range(rows)]
for coord in coords:
    x1, y1, x2, y2 = coord
    for x in range(x1, x2):
        for y in range(y1, y2):
            grid[y][x] = 1

visited = [[False] * cols for _ in range(rows)]
dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def dfs(r,c):
    visited[r][c] = True
    area = 1

    for d in dirs:
        nr, nc = r + d[0], c + d[1]

        if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == 0:
            area += dfs(nr, nc)
    return area

areas = []
cnt = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 0 and not visited[r][c]:
            areas.append(dfs(r,c))
            cnt += 1
areas.sort()
print(cnt)
print(' '.join(map(str, areas)))