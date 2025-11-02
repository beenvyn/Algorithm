def solution(array, commands):
    answer = []
    n = len(array)
    
    for c in commands:
        start, end, get = c
        new_arr = sorted(array[start-1:end])
        answer.append(new_arr[get-1])
    return answer