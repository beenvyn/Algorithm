from collections import Counter

def solution(want, number, discount):
    answer = 0
    want_cnt = {w : n for w, n in zip(want, number)}
    cur_cnt = Counter(discount[:10])
    
    # 총 (len(discount) - 10 + 1)개의 창을 검사
    for i in range(len(discount) - 9):
        if all(want_cnt[x] == cur_cnt[x] for x in want_cnt):
            answer += 1
        
        # 다음 창 준비
        if i + 10 < len(discount):
            out_item = discount[i]
            in_item = discount[i+10]
            
            cur_cnt[out_item] -= 1
            if in_item in cur_cnt:
                cur_cnt[in_item] += 1
            else:
                cur_cnt[in_item] = 1
        
    return answer