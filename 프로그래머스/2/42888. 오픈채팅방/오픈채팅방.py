def solution(record):
    answer = []
    nicknames = {}
    
    # 최종 닉네임 저장
    for r in record:
        arr = r.split()
        action = arr[0]
        if action == 'Enter' or action == 'Change':
            user_id, nickname = arr[1], arr[2]
            nicknames[user_id] = nickname
    
    # 출력 생성
    for r in record:
        arr = r.split()
        action = arr[0]
        if action == 'Enter':
            user_id, nickname = arr[1], arr[2]
            answer.append(nicknames[user_id] + '님이 들어왔습니다.')
        elif action == 'Leave':
            user_id = arr[1]
            answer.append(nicknames[user_id] + '님이 나갔습니다.')

    return answer