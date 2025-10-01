import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
max_height = max(map(max, grid))
answer = 1

def dfs(r,c):
    visited[r][c] = True

    for d in dirs:
        nr, nc = r + d[0], c + d[1]

        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > h and not visited[nr][nc]:
            dfs(nr, nc)

for h in range(1, max_height + 1):
    visited = [[False] * n for _ in range(n)]
    cnt = 0

    for r in range(n):
        for c in range(n):
            if grid[r][c] > h and not visited[r][c]:
                dfs(r, c)
                cnt += 1
    answer = max(answer, cnt)
    
print(answer)

