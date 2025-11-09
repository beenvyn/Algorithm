from collections import Counter

def solution(want, number, discount):
    answer = 0
    want_cnt = {w : n for w, n in zip(want, number)}

    # 총 (len(discount) - 10 + 1)개의 창을 검사
    for i in range(len(discount) - 9):
        if want_cnt == Counter(discount[i:i+10]):
            answer += 1
        
    return answer