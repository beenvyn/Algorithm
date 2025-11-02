def solution(n, times):
    answer = 0
    left = min(times)
    right = max(times) * n
    
    while left <= right:
        checked = 0
        mid = (left + right) // 2
        for time in times:
            checked += mid // time
        
            if checked >= n:
                break
    
        if checked >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer