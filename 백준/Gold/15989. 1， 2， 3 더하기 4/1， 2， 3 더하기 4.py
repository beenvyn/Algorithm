import sys
input = sys.stdin.readline

T = int(input())
ns = [int(input()) for _ in range(T)]
max_n = max(ns)

dp = [0] * (max_n+1) # dp[i]: 1,2,3를 더해서 i를 만드는 방법의 수
dp[0] = 1 # 아무것도 안쓰는 방법 1가지

for num in (1,2,3): # 1만 쓸 수 있는 세상에서 경우의 수 채우기 -> 1,2를 쓸 수 있는 세상에서 -> 1,2,3을 쓸 수 있는 세상에서
    for i in range(num,max_n+1):
        dp[i] += dp[i-num] # i-num을 만드는 방법에 num을 하나 더 붙인 것
    
print('\n'.join(str(dp[n]) for n in ns))