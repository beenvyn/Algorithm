def solution(clothes):
    answer = 1
    choices = {}
    
    for _, opt in clothes:
        if opt not in choices:
            choices[opt] = 0
        choices[opt] += 1
    
    for val in choices.values():
        answer *= (val + 1)

    return answer - 1