def solution(n, t, m, p):
    dic = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    
    # n진수로 num을 변환
    def get_base(num):
        if num == 0:
            return '0'
        
        res = ''
        while num > 0:
            x = num % n
            num //= n
            if x >= 10:
                res += dic[x]
            else:
                res += str(x)
        return res[::-1]
    
    result = [] # n진법으로 변환 후 한 자리로 분해한 결과
    num = 0 # 변환하는 숫자
        
    while len(result) < t * m + 1:
        temp = get_base(num)
        result.extend([t for t in temp])
        num += 1
    
    answer = ''
    for i in range(p - 1, t * m , m):
        answer += result[i]
    
    return answer