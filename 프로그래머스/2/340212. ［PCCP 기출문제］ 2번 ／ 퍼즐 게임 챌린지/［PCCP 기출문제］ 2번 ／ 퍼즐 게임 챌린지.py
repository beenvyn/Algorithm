def solution(diffs, times, limit):
    def get_time(level):
        time = times[0] # 0번 퍼즐은 이전 퍼즐이 없으므로
        for i in range(1, len(diffs)):
            if diffs[i] > level:
                time += (times[i] + times[i-1]) * (diffs[i] - level)
            time += times[i]
            # 가지치기(시간 초과면 더 볼 필요 없음)
            if time > limit:
                return time
        return time
    
    lo, hi = 1, max(diffs)
    answer = 0
    
    while lo <= hi:
        mid = (lo + hi) // 2
        if get_time(mid) <= limit: # 더 낮은 숙련도로도 가능한지 확인해야 하므로 범위를 왼쪽으로 줄임
            hi = mid - 1
            answer = mid
        else: # 제한 시간을 넘기니까 숙련도를 올려줘야 함
            lo = mid + 1
        
    return answer