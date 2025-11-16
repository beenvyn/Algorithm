def solution(n):
    answer = 0
    start, end = 0, 0
    nums = list(range(1,n+1))
    total = 1
    
    while start <= end:
        if total < n:
            end += 1
            total += nums[end]
        elif total > n:
            total -= nums[start]
            start += 1
        else:
            answer += 1
            total -= nums[start]
            start += 1

    return answer