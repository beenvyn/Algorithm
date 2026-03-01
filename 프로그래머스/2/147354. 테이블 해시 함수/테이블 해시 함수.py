def solution(data, col, row_begin, row_end):
    sorted_data = sorted(data, key=lambda x:(x[col - 1], -x[0]))
    
    S = []
    for i in range(row_begin, row_end + 1):
        temp = 0
        for d in sorted_data[i-1]:
            temp += d % i
        S.append(temp)
    
    answer = S[0]
    for s in S[1:]:
        answer = answer ^ s
        
    return answer