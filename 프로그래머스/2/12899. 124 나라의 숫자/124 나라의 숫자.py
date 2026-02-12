def solution(n):
    answer = []
    digits = ['1', '2', '4']
    
    while n > 0:
        n -= 1
        answer.append(digits[n % 3])
        n //= 3
        
    return ''.join(reversed(answer))