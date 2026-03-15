def solution(name):
    answer = 0
    n = len(name)
    
    # 알파벳 이동
    for c in name:
        answer += min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)
    
    # 커서 이동
    move = n - 1
    # 각 인덱스별로 여기서 꺾으면 이동이 얼만지 계산
    for i in range(n - 1):
        # i 다음 위치부터 연속된 A 구간 찾기
        # A는 이미 'A'라서 바꿀 필요가 없으므로 굳이 방문하지 않아도 됨
        next = i + 1
        while next < n and name[next] == 'A':
            next += 1
        
        # 앞에 먼저 처리하고 다시 맨 앞으로 가서 매 뒤로 이동 후 뒤에 처리하는 경우
        # 맨 앞에서 맨 뒤로 이동해서 뒤 먼저 처리하고 다시 앞으로 이동해서 앞 처리하는 경우
        move = min(move, i * 2 + n - next, (n - next) * 2 + i)
            
    return answer + move