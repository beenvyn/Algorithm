def solution(msg):
    answer = []
    dic = {chr(64 + i): i for i in range(1, 27)}
    idx = 27 # 다음에 들어갈 인데스
    
    i = 0 # 사전 찾기를 시작할 인덱스
    while i < len(msg):
        # 일치하는 가장 긴 문자열 찾기
        w = msg[i]
        j = i + 1
        while j < len(msg) and w + msg[j] in dic:
            w += msg[j]
            j += 1
        
        # 찾은 문자열 번호 출력
        answer.append(dic[w])
        
        # 다음 글자가 있으면 새 문자열 사전에 추가
        if j < len(msg):
            dic[w + msg[j]] = idx
            idx += 1
        
        # 다음 탐색 시작 위치
        i = j
            
    return answer