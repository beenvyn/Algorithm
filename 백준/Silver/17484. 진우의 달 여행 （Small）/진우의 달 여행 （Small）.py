import sys
input = sys.stdin.readline

rows, cols = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(rows)]

# 왼쪽 위 대각선에서 온 경우, 위에서 온 경우, 오른쪽 위 대각선에서 온 경우
dp = [[[float('inf')] * 3 for _ in range(cols)] for _ in range(rows)]

# 첫 행 초기화
for c in range(cols):
    for d in range(3):
        dp[0][c][d] = grid[0][c]

for r in range(1, rows):
    for c in range(cols):
        # 왼쪽에서 오는 경우
        if c > 0:
            dp[r][c][0] = min(dp[r-1][c-1][1], dp[r-1][c-1][2]) + grid[r][c]
        
        # 위에서 오는 경우
        dp[r][c][1] = min(dp[r-1][c][0], dp[r-1][c][2]) + grid[r][c]

        # 오른쪽에서 오는 경우
        if c < cols - 1:
            dp[r][c][2] = min(dp[r-1][c+1][0], dp[r-1][c+1][1]) + grid[r][c]

min_val = float('inf')
for c in range(cols):
    for d in range(3):
        min_val = min(min_val, dp[-1][c][d])

print(min_val)