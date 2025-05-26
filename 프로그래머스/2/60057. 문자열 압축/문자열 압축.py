def solution(s):
    answer = len(s)
    
    for unit in range(1, len(s) // 2 + 1):
        word = ''
        prev = s[:unit]
        cnt = 1
        
        for i in range(unit, len(s), unit):
            if prev == s[i:i+unit]:
                cnt += 1
            else:
                word += str(cnt) + prev if cnt > 1 else prev
                prev = s[i:i+unit]
                cnt = 1
        word += str(cnt) + prev if cnt > 1 else prev
        answer = min(len(word), answer)
    return answer