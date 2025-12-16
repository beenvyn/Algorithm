def solution(s):
    cnt = 0
    zero_cnt = 0
    
    while s != '1':
        n = len(s)
        cur_zero = s.count('0')
        s = bin(n - cur_zero)[2:]
        
        zero_cnt += cur_zero
        cnt += 1
    
    return [cnt, zero_cnt]