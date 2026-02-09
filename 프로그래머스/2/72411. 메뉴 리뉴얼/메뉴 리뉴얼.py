def solution(orders, course):
    answer = []
    menu_cnt = {} # 메뉴 조합 : 주문 수

    def combs(order, length, idx, menu):
        if len(menu) == length:
            if menu not in menu_cnt:
                menu_cnt[menu] = 0
            menu_cnt[menu] += 1
            return
        
        for i in range(idx, len(order)):
            combs(order, length, i + 1, menu + order[i])
            
    for order in orders:
        order = ''.join(sorted(order)) # 'AC'랑 'CA'를 다르게 보는 것 방지 
        for length in course:
            if length <= len(order):
                combs(order, length, 0, '')
    
    for c in course:
        candidates = [(menu, cnt) for menu, cnt in menu_cnt.items() if len(menu) == c and cnt >= 2]
        if not candidates:
            continue
        max_cnt = max(cnt for menu, cnt in candidates)
        answer.extend([menu for menu, cnt in candidates if cnt == max_cnt])
        
    return sorted(answer)