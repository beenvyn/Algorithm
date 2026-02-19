def solution(s):
    n = len(s) 
    answer = n
    
    for l in range(1, int(n//2) + 1):
        prev = s[:l]
        cnt = 1
        word = ''
        for i in range(l, n, l):
            cur_word = s[i:i+l]
            if prev == cur_word:
                cnt += 1
            else:
                word += str(cnt) + prev if cnt > 1 else prev
                prev = cur_word
                cnt = 1
        word += str(cnt) + prev if cnt > 1 else prev
        answer = min(answer, len(word))
                
    return answer