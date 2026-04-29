def solution(stones, k):
    answer = 0
    
    def possible(n):
        cnt = 0 # n번째 사람이 연속으로 못 밟는 돌의 개수
        
        for stone in stones:
            # n명이 건널 수 있으려면, n번째 사람이 밟을 돌은 n 이상이어야 함
            if stone < n:
                cnt += 1
            else:
                cnt = 0
            
            if cnt >= k:
                return False
            
        return True
        
    # 건널 수 있는 인원
    l, r = 0, max(stones)
    
    while l <= r:
        mid = (l + r) // 2
        
        if possible(mid):
            answer = max(answer, mid)
            l = mid + 1
        else:
            r = mid - 1
        
    return answer