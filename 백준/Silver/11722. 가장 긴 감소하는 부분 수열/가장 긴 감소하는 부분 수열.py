import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [1] * n # dp[i] : nums[i]를 마지막 원소로 하는 '감소하는 부분 수열'의 길이

for i in range(1,n):
    for j in range(i):
        if nums[i] < nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))