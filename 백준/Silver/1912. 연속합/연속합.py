import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# dp[i]: i에서 끝나는 연속 부분수열의 최대 합
dp = [0] * n
dp[0] = arr[0]

for i in range(1, n):
    dp[i] = max(arr[i], dp[i-1] + arr[i])

print(max(dp))