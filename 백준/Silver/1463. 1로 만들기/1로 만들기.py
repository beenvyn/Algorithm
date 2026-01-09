import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1) # dp[i]: i를 1로 만드는데 필요한 최소 연산 횟수

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i // 2] + 1, dp[i])
    if i % 3 == 0:
        dp[i] = min(dp[i // 3] + 1, dp[i])

print(dp[n])