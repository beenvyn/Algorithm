def solution(n, stations, w):
    answer = 0
    deliver = w * 2 + 1 # 전파 거리 
    idx = 1 # 현재 아파트
    
    for station in stations:
        dist = station - w - idx
        answer += (dist + deliver - 1) // deliver
        idx = station + w + 1
        
    if idx <= n:
        dist = n - idx + 1
        answer += (dist + deliver - 1) // deliver
        
    return answer