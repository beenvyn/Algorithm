def solution(n, s):
    # 기본값을 s // n으로 n개 깔기
    # 나머지 s % n만큼 뒤에서부터 +1
    
    if s < n:
        return [-1]
    
    base = s // n
    rem = s % n
    
    answer = [base] * n
    
    for i in range(rem):
        answer[n - i - 1] += 1
    
    return answer