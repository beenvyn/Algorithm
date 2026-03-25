def solution(expression):
    answer = 0
    opts = ['+', '-', '*']
    
    # 수식 파싱
    parsed_exp = []
    str_num = ''
    
    for x in expression:
        if x in opts:
            parsed_exp.append(int(str_num))
            parsed_exp.append(x)
            str_num = ''
        else:
            str_num += x
    parsed_exp.append(int(str_num))
    
    # 계산 함수
    def cal(order):
        arr = parsed_exp[:]
        
        for op in order:
            stack = []
            i = 0
            while i < len(arr):
                if arr[i] == op:
                    a = stack.pop()
                    b = arr[i + 1]
                    
                    if op == '+':
                        stack.append(a + b)
                    elif op == '-':
                        stack.append(a - b)
                    else:
                        stack.append(a * b)
                        
                    i += 2
                else:
                    stack.append(arr[i])
                    i += 1
            arr = stack
            
        return abs(arr[0])
    
    visited = [False] * 3
    # 연산자 우선순위 순열
    def permutation(cur):
        nonlocal answer
        
        if len(cur) == 3:
            answer = max(answer, cal(cur))
            return
            
        for i in range(3):
            if not visited[i]:
                visited[i] = True
                permutation(cur + [opts[i]])
                visited[i] = False
    
    permutation([])
    
    return answer