def solution(storey):
    answer = 0
    # 아이디어: 맨 끝(1의 자리)부터 보고,
    # - 아래로 내려서 0으로 만들 지(그 자리 숫자만큼 -1 버튼) 
    # - 위로 올려서 10으로 만들 지(10 - 그 자리 숫자만큼 +1 버튼, 상위 자리에 캐리)를 더 싼 쪽으로 선택한다.
    
    while storey:
        remainder = storey % 10 # 현재(가장 낮은) 자리 숫자
        
        # 6 ~ 9
        if remainder > 5:
            answer += (10 - remainder)
            storey += 10  # 상위 자리로 캐리를 만들기 위해 10을 더해 둔다
        # 0 ~ 4
        elif remainder < 5:
            answer += remainder
        # 5
        else: # 올리기와 내리기가 동일한 비용이므로 다음 자리 숫자를 보고 판단
            # - 다음 자리가 5 이상이면, 올림(캐리) 쪽이 이후 자리들에서도 유리한 경우가 많음
            # - 아니면 내리기 선택
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += remainder # 5회 버튼(올리기든 내리기든 비용은 동일)
        # 현재 자리는 정리했으므로 상위 자리로 이동
        storey //= 10

    return answer
            