def solution(n, k):
    
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True
    
    digits = []
    while n > 0:
        digits.append(str(n % k))
        n //= k
    s = ''.join(reversed(digits))
    
    answer = 0
    for part in s.split('0'):
        if not part: # 빈 문자열 스킵
            continue
        val = int(part)
        if is_prime(val):
            answer += 1
    
    return answer