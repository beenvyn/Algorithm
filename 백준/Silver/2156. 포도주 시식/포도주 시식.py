import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

dp = [0] * (n + 1) # dp[i]: i 번째까지 최대 포도주 양
if n == 1:
    print(arr[0])
    exit()
elif n == 2:
    print(arr[0]+arr[1])
    exit()
    
dp[1] = arr[0]
dp[2] = arr[0] + arr[1]

for i in range(3, n + 1):
    dp[i] = max(dp[i-1], arr[i-1] + dp[i-2], arr[i-1] + arr[i-2] + dp[i-3])  # i 안 마심, i만 마심, i-1이랑 i만 마심

print(dp[n])