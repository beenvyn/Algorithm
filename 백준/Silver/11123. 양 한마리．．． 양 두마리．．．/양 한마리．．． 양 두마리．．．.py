import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(r, c):
    visited[r][c] = True

    for d in dirs:
        nr, nc = r + d[0], c + d[1]

        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '#' and not visited[nr][nc]:
            dfs(nr, nc)

for _ in range(T):
    rows, cols = map(int, input().split())
    grid = [input().rstrip() for _ in range(rows)]

    visited = [[False] * cols for _ in range(rows)]
    cnt = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '#' and not visited[r][c]:
                dfs(r, c)
                cnt += 1
    
    print(cnt)