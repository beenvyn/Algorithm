def solution(order):
    answer = 0
    n = len(order)
    cur_box = 1
    stack = []
    
    for i in range(n):
        if cur_box == order[i]:
            answer += 1
            cur_box += 1
        elif cur_box < order[i]:
            while cur_box < order[i]:
                stack.append(cur_box)
                cur_box += 1
            answer += 1
            cur_box += 1
        else:
            if stack and stack[-1] == order[i]:
                stack.pop()
                answer += 1
            else:
                return answer
    return answer