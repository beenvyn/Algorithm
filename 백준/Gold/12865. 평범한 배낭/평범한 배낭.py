import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (K + 1) # dp[i]: 무게 i만큼 넣었을 때 얻을 수 있는 최대 가치

for w, v in items:
    for i in range(K, w - 1, -1): # 물건을 한 번만 담을 수 있으므로 뒤에서 돌리기 
        dp[i] = max(dp[i], dp[i - w] + v)

print(dp[K])