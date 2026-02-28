def solution(n, q, ans):
    answer = 0
    q_sets = [set(row) for row in q]
    m = len(q)
    
    def check(case):
        for i in range(m):
            if len(case & q_sets[i]) != ans[i]:
                return False
        return True
                        
    # 1부터 n까지 5개의 숫자 선택
    def comb(idx, cur):
        nonlocal answer
        if len(cur) == 5:
            if check(set(cur)):
                answer += 1
            return
        
        for i in range(idx, n + 1):
            comb(i + 1, cur + [i])
    
    comb(1, [])
    return answer