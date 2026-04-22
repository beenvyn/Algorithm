def solution(cols, rows, puddles):
    MOD = 1000000007

    # dp[r][c] : (r, c)까지 오는 방법의 수
    dp = [[0] * cols for _ in range(rows)]
    dp[0][0] = 1
    
    puddles_arr = []
    for x, y in puddles:
        puddles_arr.append([y - 1, x - 1])
    
    for r in range(rows):
        for c in range(cols):
            if [r, c] in puddles_arr:
                continue
            elif r == 0 and c == 0:
                continue
            else:
                up = dp[r - 1][c] if r > 0 else 0
                left = dp[r][c - 1] if c > 0 else 0
                dp[r][c] = (up + left) % MOD
    
    return dp[rows - 1][cols - 1]