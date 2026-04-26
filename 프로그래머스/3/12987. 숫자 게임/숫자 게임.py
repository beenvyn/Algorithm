def solution(A, B):
    answer = 0
    A.sort() 
    B.sort() 
    i, j = 0, 0 # A 포인터, B 포인터
    
    # 이길 수 있으면 최소한으로 이기고, 못 이기면 버린다
    for _ in range(len(A)):
        if A[i] < B[j]:
            answer += 1
            i += 1
            j += 1
        else: # 이길 수 없으면 B의 작은 숫자는 버리고 다음 B를 봄
            j += 1
        
    return answer