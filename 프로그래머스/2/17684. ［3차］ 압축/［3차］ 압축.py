def solution(msg):
    answer = []
    dic = {chr(64 + i) : i  for i in range(1, 27)}
    idx = 26
    
    i = 0
    while i < len(msg):
        j = i + 1

        # 일치하는 가장 긴 문자열 찾기
        while j <= len(msg) and msg[i:j] in dic:
            j += 1
        
        w = msg[i:j-1]
        answer.append(dic[w])
        
        # 사전에 새로운 단어 추가
        if j <= len(msg):
            new_word = msg[i:j]
            idx += 1
            dic[new_word] = idx
        
        # 다음 탐색 위치 지정
        i += len(w)

    return answer