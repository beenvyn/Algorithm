import sys
input = sys.stdin.readline

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

dp = [[0,0,0] for _ in range(N)] # dp[i][c] = i번째 집을 색 c로 칠했을 때의 최소 비용

dp[0] = costs[0]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

print(min(dp[N - 1]))