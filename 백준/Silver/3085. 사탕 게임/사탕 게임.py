import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
grid = [input().rstrip() for _ in range(N)]

dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
visited = set() # (사탕1의 좌표, 사탕2의 좌표)

def get_cnt(r1, c1, r2, c2):
    visited.add((r1, c1, r2, c2))
    # 사탕 두 개 위치 교환
    new_grid = [list(row) for row in grid] 
    new_grid[r1][c1], new_grid[r2][c2] = new_grid[r2][c2], new_grid[r1][c1]
    max_cnt = 0

    # 행 탐색
    for r in range(N):
        cnt = 1
        for c in range(1, N):
            if new_grid[r][c - 1] == new_grid[r][c]:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 1
        max_cnt = max(max_cnt, cnt)
        
    # 열 탐색
    for c in range(N):
        cnt = 1
        for r in range(1, N):
            if new_grid[r-1][c] == new_grid[r][c]:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 1
        max_cnt = max(max_cnt, cnt)
    return max_cnt

answer = 0
for r in range(N):
    for c in range(N):
        for d in dirs:
            nr, nc = r + d[0], c + d[1]
            # 인접하면서 색이 다른 사탕 두 개 전달
            if 0 <= nr < N and 0 <= nc < N and grid[r][c] != grid[nr][nc] and (r, c, nr, nc) not in visited:
                answer = max(answer, get_cnt(r, c, nr, nc))
print(answer)