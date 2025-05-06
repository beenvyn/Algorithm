def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stack = []
    idx = 0
    
    while idx < n:
        for i in range(n):
            while stack and numbers[stack[-1]] < numbers[idx]:
                x = stack.pop()
                answer[x] = numbers[idx]
            stack.append(idx)
            idx += 1
        
    return answer