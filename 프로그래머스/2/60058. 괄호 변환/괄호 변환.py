def solution(p):
    # 올바른 괄호 문자열인지 판단하는 함수
    def is_correct(brackets):
        stack = []
        for b in brackets:
            if stack:
                if b == ')' and stack[-1] == '(':
                    stack.pop()
                    continue
            stack.append(b)
        return False if stack else True
    
    # u, v로 분리하는 함수
    def seperate(brackets):
        cnt = {'(': 0, ')': 0}
        i = 0
        
        while i < len(brackets):
            if i > 0 and cnt[')'] == cnt['(']:
                break
                
            b = brackets[i]
            cnt[b] += 1
            i += 1
            
        u = brackets[:i]
        v = '' if i == len(brackets) - 1 else brackets[i:]
        return u, v
    
    # 뒤집는 함수
    def reverse(u):
        return ''.join('(' if x == ')' else ')' for x in u[1:-1])
    
    # 재귀 함수
    def transform(w):
        if w == '':
            return ''
        
        u, v = seperate(w)
        
        if is_correct(u): # 3번
            return u + transform(v)
        else: # 4번
            return '(' + transform(v) +')' + reverse(u)
            
    return transform(p)