import sys
input = sys.stdin.readline

while True:
    n, m = map(float, input().split())
    n, m = int(n), int(m * 100 + 0.5) # 센트 단위 정수로 변환

    if n == 0 and m == 0:
        break

    sweets = []
    for _ in range(n):
        c, p = map(float, input().split())
        c, p = int(c), int(p * 100 + 0.5)
        sweets.append((c, p))

    # dp[i]: 가격을 i만큼 썼을 때의 최대 칼로리
    dp = [0] * (m + 1)

    for c, p in sweets:
        for i in range(p, m + 1):
            dp[i] = max(dp[i - p] + c, dp[i])
    
    print(dp[m])