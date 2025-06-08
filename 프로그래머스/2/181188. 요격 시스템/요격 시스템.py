def solution(targets):
    answer = 0
    # [[1, 4], [4, 5], [3, 7], [4, 8], [5, 12], [11, 13], [10, 14]]
    targets.sort(key = lambda x:(x[1], x[0]))
    last_shot = -1
    
    for start, end in targets:
        if start >= last_shot:
            answer += 1
            last_shot = end
    
    return answer