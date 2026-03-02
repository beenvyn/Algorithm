def solution(points, routes):
    answer = 0
    logs = []
    
    # 이동 경로 생성 함수
    def get_logs(s, e):
        cur_log = []
        r1, c1 = s
        r2, c2 = e
        cur_log.append((r1, c1))
        
        while r1 != r2:
            if r1 > r2:
                r1 -= 1
            else:
                r1 += 1
            cur_log.append((r1, c1))
        
        while c1 != c2:
            if c1 > c2:
                c1 -= 1
            else:
                c1 += 1
            cur_log.append((r1, c1))
        return cur_log
        
    # 각 객체별 이동 경로 생성
    for route in routes:
        full_log = []
        for i in range(len(route) - 1):
            start, end = route[i], route[i + 1]
            seg = get_logs(points[start - 1], points[end - 1])
            
            # 이전 구간과 이어붙일 때 중복 시작점 제거
            if i > 0:
                seg = seg[1:]
                
            full_log.extend(seg)
        logs.append(full_log)
                
    # 가장 긴 시간 구하기
    max_time = max(len(l) for l in logs)
    
    # 시간별 충돌 체크
    for t in range(max_time):
        dir_cnt = {}
        for log in logs:
            # 도착 후에는 더이상 카운트 하지 않음
            if t >= len(log):
                continue
                
            r, c = log[t] 
            if (r, c) not in dir_cnt:
                dir_cnt[(r, c)] = 0
            dir_cnt[(r, c)] += 1
        
        for cnt in dir_cnt.values():
            if cnt >= 2:
                answer += 1
            
    return answer