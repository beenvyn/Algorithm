def solution(storey):
    answer = 0
    
    while storey > 0:
        digit = storey % 10
        next_digit = (storey // 10) % 10
        
        if digit > 5: # 현재 자리 숫자가 5보다 크면 올림
            answer += 10 - digit
            storey += 10
        elif digit == 5: # 현재 자리 숫자가 5면 다음 자리 보고 결정
            if next_digit >= 5:
                storey += 10
            answer += 5
        else: # 현재 자리 숫자가 5보다 작으면 내림
            answer += digit
        
        storey //= 10

    return answer