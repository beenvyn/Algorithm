def solution(s):
    answer = 0
    n = len(s)
    
    for i in range(n-1):
        stack = []
        new_s = s[1:] + s[0]
        
        for c in s:
            if c in ')}]' and len(stack) > 0:
                if c == ')' and stack[-1] == '(':
                    stack.pop()
                    continue
                if c == ']' and stack[-1] == '[':
                    stack.pop()
                    continue
                if c == '}' and stack[-1] == '{':
                    stack.pop()
                    continue
            stack.append(c)
        
        if not stack:
            answer += 1
        
        s = new_s

    return answer