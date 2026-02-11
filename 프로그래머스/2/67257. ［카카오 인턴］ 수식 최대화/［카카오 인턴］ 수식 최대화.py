def solution(expression):
    answer = 0
    tokens = []
    num = ''
    
    for x in expression:
        if x.isdigit():
            num += x
        else:
            tokens.append(int(num))
            tokens.append(x)
            num = ''
    tokens.append(int(num))
    
    def apply(a, op, b):
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        else:
            return a * b
    
    # 숫자, 연산자 분리
    def calculate(ops):
        cur = tokens[:]
        # 우선순위에 따라 연산자 하나씩 처리
        for op in ops:
            stack = []
            i = 0
            while i < len(cur):
                if cur[i] == op:
                    left = stack.pop()
                    right = cur[i+1]
                    stack.append(apply(left, op, right))
                    i += 2 # 연산자 + 숫자 소비
                else:
                    stack.append(cur[i])
                    i += 1
            cur = stack # 이번 연산자 처리 결과를 다음 단계로 넘김
        return abs(cur[0])
        
    operators = ['+', '-', '*']
    visited = [False] * 3
    def permutation(cur):
        nonlocal answer
        
        if len(cur) == 3:
            answer = max(answer, calculate(cur))
            return
        
        for i in range(3):
            if not visited[i]:
                visited[i] = True
                cur.append(operators[i])
                permutation(cur)
                visited[i] = False
                cur.pop()
        
    permutation([])
    
    return answer