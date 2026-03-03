def solution(cap, n, deliveries, pickups):
    answer = 0
    d_remain = 0 # 지금까지 처리해야 할 '배달' 총량
    p_remain = 0 # 지금까지 처리해야 할 '수거' 총량
    
    for i in range(n-1, -1, -1):
        # 이 거리까지 가야 처리해야 할 총 물량을 누적
        d_remain += deliveries[i]
        p_remain += pickups[i]
        
        # 양수면 아직 이 거리까지 처리 못한 물량이 남아있다
        # 음수면 이미 이전에 간 김에 처리됐다는 뜻
        while d_remain > 0 or p_remain > 0:
            # 한 번 갈 때 cap만큼 배달/수거 가능
            d_remain -= cap
            p_remain -= cap
            answer += (i + 1) * 2
    
    return answer