def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = [] # 스택에 가격이 떨어지지 않은 주식들의 인덱스만 남김
    
    for i in range(n):
        while stack and prices[stack[-1]] > prices[i]: # 가격이 떨어진 경우
            top = stack.pop()
            answer[top] = i - top
        stack.append(i)
    
    while stack:
        x = stack.pop()
        answer[x] = n - x - 1

    return answer