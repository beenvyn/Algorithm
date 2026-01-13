import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input().rstrip()) for _ in range(n)]
coins = list(set(coins)) # 중복 제거

dp = [float('inf')] * (k + 1) # dp[i]: 금액 i를 만드는데 필요한 최소 동전의 개수
dp[0] = 0

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)
print(dp[k] if dp[k] != float('inf') else -1)