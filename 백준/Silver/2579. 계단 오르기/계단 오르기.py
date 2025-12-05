import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

dp = [0] * (n + 1) # dp[i]: i번째 계단에 도착했을 때 얻을 수 있는 최대 점수

if n == 1:
    print(arr[0])
    exit()
elif n == 2:
    print(arr[0] + arr[1])
    exit()

dp[1] = arr[0]
dp[2] = arr[0] + arr[1]

for i in range(3, n + 1):
    dp[i] = max(arr[i-1] + arr[i-2] + dp[i-3], arr[i-1] + dp[i-2])

print(dp[n])