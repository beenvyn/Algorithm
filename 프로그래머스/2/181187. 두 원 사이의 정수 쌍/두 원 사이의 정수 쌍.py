import math

def solution(r1, r2):
    answer = 0
    
    # r1² ≤ x² + y² ≤ r2²
    # x를 기준으로 가능한 y의 최대/최소 범위 구하기
    for x in range(1, r2 + 1):
        # 큰 원 안쪽에서 가능한 y의 최댓값
        y_max = int(math.sqrt(r2**2 - x**2))
        
        if x < r1: # x가 작은 원 안쪽인 경우 y의 값은 작은 원을 넘어야 됨
            y_min = math.ceil(math.sqrt(r1**2 - x**2))
        else: # x가 작은 원 바깥쪽인 경우 y는 0이어도 상관없음
            y_min = 0
            
        # 해당 x에서 가능한 정수 y 개수
        answer += (y_max - y_min + 1)
    
    return answer * 4


            
    