import math

def solution(k, d):
    answer = 0
    
    # x가 정해지면 y도 정해짐
    for x in range(0, d + 1, k):
        max_y = int(math.sqrt(d**2 - x**2))
        # 0~max_y 중 k의 배수가 되는 y의 개수 세기. 0도 포함해야 되니까 + 1을 해줌
        answer += max_y // k + 1 
        
    return answer