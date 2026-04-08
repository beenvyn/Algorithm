import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

# 증가 순서를 유지하는 최대 부분 수열 찾기
# dp[i]: nums[i]를 마지막으로 하는 가장 긴 부분 수열
dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[j] + 1, dp[i])

print(N - max(dp))