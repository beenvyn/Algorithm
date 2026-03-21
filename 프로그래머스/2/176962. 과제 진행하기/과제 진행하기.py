def solution(plans):
    answer = []
    
    def to_mins(s):
        h, m = map(int, s.split(':'))
        return h * 60 + m
    
    parsed_plans = [] # [과제 이름, 시작 시간, 실행 시간]
    for name, start, playtime in plans:
        parsed_plans.append([name, to_mins(start), int(playtime)])
    
    parsed_plans.sort(key=lambda x:x[1]) # 시작 시간 빠른 순으로 정렬
    
    stack = [] # [멈춰둔 과제 이름, 남은 시간]
    
    for i in range(len(plans) - 1):
        name, start, playtime = parsed_plans[i] # 현재 과제
        available = parsed_plans[i + 1][1] - start # 현재 과제에 할당된 시간
        
        if available >= playtime: # 현재 과제 끝낼 수 있음
            answer.append(name)
            remain_time = available - playtime
            
            while remain_time > 0 and stack:
                prev_name, prev_time = stack.pop()
                if remain_time >= prev_time: # 멈춘 과제의 남은 실행 시간이 다음 과제까지 남은 시간보다 적으면
                    remain_time -= prev_time
                    answer.append(prev_name) # 멈춘 과제 다 처리
                else:
                    stack.append([prev_name, prev_time - remain_time])
                    remain_time = 0
        else:
            stack.append([name, playtime - available])     
    
    answer.append(parsed_plans[-1][0]) # 마지막 과제는 무조건 끝낼 수 있음
    
    while stack: # 한 바퀴 돌렸을 때 완성 못한 과제들
        name, _ = stack.pop()
        answer.append(name)

    return answer