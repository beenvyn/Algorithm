def solution(n, money):
    dp = [0] * (n + 1) # dp[i]: i를 만들 수 있는 방법의 수
    dp[0] = 1 # 0원을 만드는 방법 -> 아무것도 안 쓰는 1가지
    
    for m in money:
        for i in range(m, n + 1):
            dp[i] += dp[i - m]
    
    return dp[n]