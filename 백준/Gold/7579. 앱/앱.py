import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

# dp[c] = 비용 c로 확보할 수 있는 최대 메모리
sum_cost = sum(costs)
dp = [0] * (sum_cost + 1)

for i in range(N):
    memory, cost = memories[i], costs[i]
    for c in range(sum_cost, cost - 1, -1):
        dp[c] = max(dp[c], dp[c - cost] + memory)

for c in range(sum_cost + 1):
    if dp[c] >= M:
        print(c)
        break