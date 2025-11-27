import math

def solution(n,a,b):
    answer = 0
    
    while a != b:
        a = (a + 1) // 2   # 다음 라운드에서의 번호
        b = (b + 1) // 2   # 다음 라운드에서의 번호
        answer += 1        # 라운드 수 +1
    
    return answer
