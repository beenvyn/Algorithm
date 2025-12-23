import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 1) # dp[i]: 3 * i를 채우는 경우의 수
dp[0] = 1
if n >= 2:
    dp[2] = 3 # 3 * 2를 채우는 경우는 3개

if n % 2: # n이 홀수면 채우기 불가능 
    print(0)
    sys.exit()

for i in range(4, n + 1, 2):
    dp[i] = dp[i-2] * 3 # 일반적인 경우로 오른쪽 끝 3 * 2를 채우는 경우
    # 특수 케이스 누적
    for j in range(i - 4, -1, -2):
        dp[i] += dp[j] * 2

print(dp[n])