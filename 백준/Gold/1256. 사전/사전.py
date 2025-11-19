import sys
input = sys.stdin.readline

n, m, k = list(map(int,input().split()))

# dp[i][j]: 'a' i개, 'z' j개로 만들 수 있는 서로 다른 문자열의 개수
dp = [[1] * (m + 1) for _ in range(n + 1)]
# 'a'만 있는 경우 (j=0) → "aaa...a" 딱 1가지
# 'z'만 있는 경우 (i=0) → "zzz...z" 딱 1가지
# 그래서 일단 전부 1로 채워두고 점화식으로 갱신함

for i in range(1, n + 1):
    for j in range(1, m + 1):
        # 'a' i개, 'z' j개로 만들 수 있는 문자열은
        # 맨 앞에 'a'를 두고, 나머지 (i-1, j)로 만드는 경우
        # 맨 앞에 'z'를 두고, 나머지 (i, j-1)로 만드는 경우
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

if dp[n][m] < k:
    print("-1")
else:
    res = ''
    while True:
        # 더 이상 한쪽 문자가 없으면 남은 건 전부 같은 문자
        if n == 0 or m == 0:
            res += 'a' * n
            res += 'z' * m
            break

        # 맨 앞에 'a'를 하나 둔다고 가정했을 때 만들 수 있는 문자열 개수
        # 'a'를 하나 썼으니까 남은 건 (n-1)개의 a, m개의 z
        flag = dp[n-1][m] 

        # 만약 k가 flag보다 작거나 같다면 → k번째 문자열은 "앞에 'a'를 붙인 경우들" 안에 포함된다는 뜻
        if flag >= k:
            res += 'a'
            n -= 1 # 'a' 하나 썼으니 개수 줄이기
        else:
            # 만약 k가 flag보다 크다면,
            # 앞에 'a'를 붙인 경우들(dp[n-1][m]개)을 전부 건너뛴 뒤 앞에 'z'를 붙인 경우들 안에서 찾아야 한다.
            res += 'z'
            m -= 1 # 'z' 하나 썼으니 개수 줄이기
            k -= flag # 'a'로 시작하는 모든 경우(flag개)를 건너뛰었으나까 k를 그만큼 줄여서 갱신
    print(res)