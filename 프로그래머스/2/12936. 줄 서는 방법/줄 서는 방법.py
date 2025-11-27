import math

def solution(n, k):
    arr = [i for i in range(1, n + 1)] # 남은 사람
    answer = []
    
    # 모든 사람이 다 줄을 설 때까지 반복
    while arr:
        # k를 0-based index로 변환
        # n명이 줄을 설 때, 맨 앞자리를 정하면, 나머지 n-1명은 (n-1)!가지 방법으로 줄 설 수 있음.
        # 앞자리를 기준으로 몇 번째 묶음에 속하는지 계산
        x = (k - 1) // math.factorial(n - 1)
        answer.append(arr.pop(x))
        
        # 다음 실행을 위한 준비(순서 업데이트 & 남은 사람 줄이기)
        k = k % math.factorial(n - 1) # 그 묶음 안에서의 새로운 k값 (남은 순번)
        n -= 1
    
    return answer