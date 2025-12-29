import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

# dp[i]: nums의 i번째 수를 마지막 원소로 쓰는 증가 수열의 최대 길이
dp = [1] * n

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))