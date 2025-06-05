def solution(schedules, timelogs, startday):
    answer = 0

    def convert(time):
        time = str(time)
        h = time[:-2]
        m = time[-2:]
        return int(h) * 60 + int(m)
    
    # 직원 순회
    for i in range(len(schedules)):
        curday = startday - 1
        timelog = timelogs[i]
        schedule = convert(schedules[i] + 10)
        
        # 시간 순회
        for t in timelog:
            curday += 1
            
            if curday % 7 in [0, 6]:
                continue
                
            if schedule < convert(t):
                break
        else:
            answer += 1

    return answer