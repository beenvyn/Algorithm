from collections import deque

def solution(begin, target, words):
    n = len(words)
    visited = [False] * n
    que = deque([(begin, 0)])
    
    while que:
        cur_word, cnt = que.popleft()
        
        if cur_word == target:
            return cnt
        
        for i in range(n):
            if not visited[i] and sum(a != b for a, b in zip(words[i], cur_word)) == 1:
                que.append((words[i], cnt + 1))
                visited[i] = True
    
    return 0