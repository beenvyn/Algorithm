def solution(n, q, ans):
    answer = 0
    m = len(q)
    
    def check(case):
        for i in range(m):
            cnt = 0
            for x in sorted(q[i]):
                for c in case:
                    if x == c:
                        cnt += 1
            if cnt != ans[i]:
                return False
        return True
                        
    # 1부터 n까지 5개의 숫자 선택
    def comb(idx, cur):
        nonlocal answer
        if len(cur) == 5:
            if check(sorted(cur)):
                answer += 1
            return
        
        for i in range(idx, n + 1):
            comb(i + 1, cur + [i])
    
    comb(1, [])
    return answer