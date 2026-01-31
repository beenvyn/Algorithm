import sys
input = sys.stdin.readline

C, N = map(int, input().split())
ads = [list(map(int, input().split())) for _ in range(N)]

dp = [float('inf')] * (C + 100) # dp[i]: 고객 i명 이상을 늘리기 위해 필요한 돈의 최솟값
dp[0] = 0

for cost, customer in ads:
    for i in range(customer, C + 100): # i명의 고객을 만들고 싶을 때
        dp[i] = min(dp[i], dp[i - customer] + cost)

print(min(dp[C:]))