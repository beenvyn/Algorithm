def solution(plans):
    stack = [] # 멈춰둔 / 진행중이던 과제들 : [과제 이름, 실행 시간]
    answer = []
    
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(':'))
        plans[i][1] = h * 60 + m
        plans[i][2] = int(plans[i][2])
    
    plans.sort(key=lambda x:x[1])
    
    for i in range(len(plans) - 1):
        stack.append([plans[i][0], plans[i][2]]) # 현재 과제를 스택에 쌓는다(시작됨)
        gap = plans[i+1][1] - plans[i][1] # 현재 과제와 다음 과제 사이의 빈 시간
        
        # 빈 시간 동안 스택 상단 과제를 가능한 만큼 처리
        while stack and gap:
            cur_time = stack[-1][1] # 현재 과제의 남은 실행 시간
            
            if cur_time <= gap: # 다음 과제 전까지 완료 가능한 경우
                name, time = stack.pop()
                answer.append(name)
                gap -= time
            else: # 다음 과제 전까지 완료 불가능한 경우
                stack[-1][1] -= gap # 빈 시간 까지만 실행한다
                gap = 0
    
    stack.append([plans[-1][0], plans[-1][2]]) # 마지막 과제
    
    while stack: # 이후 남아있는 과제들을 LIFO 순서로 마무리
        answer.append(stack.pop()[0])

    return answer