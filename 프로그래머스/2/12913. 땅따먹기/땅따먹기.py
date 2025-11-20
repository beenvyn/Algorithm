def solution(land):
    answer = 0
    n = len(land)
    dp = [row[:] for row in land] # dp[r][c]: r행 c열까지 왔을 때 얻을 수 있는 최대 점수
    
    for r in range(1, len(land)):
        for c in range(4): # 바로 위 행(r-1)에서 같은 열(c)을 제외한 열들 중 최대값을 더함
            dp[r][c] += max(dp[r-1][k] for k in range(4) if k != c)

    return max(dp[-1])