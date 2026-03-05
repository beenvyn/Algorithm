def solution(n, times):
    answer = 0
    l, r = 0, max(times) * n # 시간(정답) 후보
    
    # T분 안에 n명 이상 심사할 수 있나?
    while l <= r:
        mid = (l + r) // 2
        
        cnt = 0
        for t in times:
            cnt += mid // t
        
        if cnt >= n:
            answer = mid
            r = mid - 1
        else:
            l = mid + 1
    return answer