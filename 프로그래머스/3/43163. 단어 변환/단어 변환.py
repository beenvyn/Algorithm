from collections import deque

def solution(begin, target, words):
    q = deque([(begin, 0)])
    visited = {w : False for w in words}
    
    while q:
        cur_word, cnt = q.popleft()
        
        if cur_word == target:
            return cnt
        
        for word in words:
            if sum([a != b for a, b in zip(cur_word, word)]) == 1 and not visited[word]:
                q.append((word, cnt + 1))
                visited[word] = True
            
    return 0
