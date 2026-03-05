def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        stack = list(skill)[::-1]
        flag = True
        for s in skill_tree:
            if s in skill: # 선행 스킬이 있는 스킬이면
                if stack and s == stack[-1]: # 순서가 맞는 경우
                    stack.pop()
                else: # 순서가 틀린 경우
                    flag = False
                    break
        if flag:
            answer += 1   
    return answer