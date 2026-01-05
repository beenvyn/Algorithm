import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

rows, cols = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(rows)]
visited = [[False] * cols for _ in range(rows)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cnt = 0
max_area = 0

def dfs(r, c):
    visited[r][c] = True
    area = 1 # 방문한 칸 수

    for d in dirs:
        nr, nc = r + d[0], c + d[1]

        if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == 1:
            area += dfs(nr, nc)
    return area

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 1 and not visited[r][c]:
            max_area = max(max_area, dfs(r, c))
            cnt += 1

print(cnt)
print(max_area)