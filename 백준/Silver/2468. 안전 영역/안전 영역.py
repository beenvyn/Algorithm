import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

max_h = max(map(max, grid))
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 1

def dfs(r, c):
    visited[r][c] = True

    for d in dirs:
        nr, nc = r + d[0], c + d[1]

        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and grid[nr][nc] > h:
            dfs(nr, nc)

for h in range(1, max_h + 1):
    visited = [[False] * N for _ in range(N)]
    cnt = 0

    for r in range(N):
        for c in range(N):
            if grid[r][c] > h and not visited[r][c]:
                dfs(r, c)
                cnt += 1
    answer = max(answer, cnt)

print(answer)   