from collections import Counter

def solution(k, tangerine):
    tan_count = sorted(Counter(tangerine).values(),reverse=True) # 귤 크기별 개수를 세고, 개수가 많은 순으로 정렬
    picked = 0
    kind = 0
    
    # 개수가 많은 크기부터 하나씩 사용
    for cnt in tan_count:
        picked += cnt
        kind += 1
        if picked >= k:
            return kind