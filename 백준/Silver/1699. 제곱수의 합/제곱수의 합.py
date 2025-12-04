import sys, math
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1) # dp[i]: i를 표현하는 제곱수 항의 최소 개수

for i in range(1, n + 1):
    dp[i] = i # 최악의 경우: 1^2를 i번 더해서 i개
    j = 1
    # i에서 가능한 모든 제곱수를 다 빼보면서 최소를 찾아야 함
    while j*j <= i:
        dp[i] = min(dp[i], dp[i - j*j] + 1) # +1은 j*j를 만들기 위해 쓴 항임
        j += 1
            
print(dp[n])