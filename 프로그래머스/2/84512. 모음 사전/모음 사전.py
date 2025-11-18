def solution(word):
    vowels = [ 'A', 'E', 'I', 'O', 'U']
    cnt = 0
    
    def dfs(cur):
        nonlocal cnt
        
        if cur:
            cnt += 1
            if cur == word:
                return True
        
        if len(cur) == 5:
            return False
            
        for ch in vowels:
            if dfs(cur + ch):
                return True
        
    dfs('')
    return cnt