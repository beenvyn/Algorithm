def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x:(x[col - 1], -x[0]))
    
    answer = 0
    for i in range(row_begin, row_end + 1):
        s_i = sum(v % i for v in data[i-1])
        answer ^= s_i
        
    return answer