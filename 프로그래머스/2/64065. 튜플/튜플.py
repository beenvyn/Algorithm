def solution(s):
    answer = []
    
    s_arr = s[2:-2].split('},{')
    s_arr.sort(key=lambda x: len(x))
    
    for i in range(len(s_arr)):
        arr = list(map(int, s_arr[i].split(',')))
        for n in arr:
            if n not in answer:
                answer.append(n)

    return answer