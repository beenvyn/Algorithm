def solution(info, n, m):
    MAX = 120
    items = len(info) # 훔쳐야하는 물건 개수
    
    # dp[a][b] = A 흔적 a, B 흔적 b 상태가 "가능한가?"
    dp = [[False] * MAX for _ in range(MAX)]
    dp[0][0] = True # 아무것도 훔치지 않은 상태는 가능
    
    # 각 물건 하나씩 처리
    for trace_a, trace_b in info:
        # 이번 물건 처리 결과를 담을 새 배열
        new_dp = [[False] * MAX for _ in range(MAX)]
        
        # 현재 가능한 모든 상태 순회
        for a in range(n):       # A 흔적은 n 미만까지만 의미 있음
            for b in range(m):   # B 흔적은 m 미만까지만 의미 있음
                if not dp[a][b]: # 이 상태가 가능하지 않으면 패스
                    continue
                
                # A가 훔치는 경우
                if trace_a + a < n:
                    new_dp[a + trace_a][b] = True
                
                # B가 훔치는 경우
                if trace_b + b < m:
                    new_dp[a][b + trace_b] = True
                
        dp = [row[:] for row in new_dp] # 이번 물건까지 반영된 결과 갱신
        
    for a in range(n): # 작은 A부터 검사 → 최초 발견이 최소
        for b in range(m):
            if dp[a][b]:
                return a
    return -1