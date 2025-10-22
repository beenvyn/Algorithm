import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())

    if n <= 3:
        print([0,1,2,4][n])
        continue

    dp = [0] * (n+1)
    dp[1], dp[2], dp[3] = 1, 2, 4

    for i in range(4,n+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    
    print(dp[n])