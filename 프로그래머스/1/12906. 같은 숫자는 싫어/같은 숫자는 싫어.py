def solution(arr):
    n = len(arr)
    cur_c = arr[0]
    answer = [cur_c]
    
    for i in range(n):
        if arr[i] == cur_c:
            continue
        else:
            answer.append(arr[i])
            cur_c = arr[i]
    
    return answer