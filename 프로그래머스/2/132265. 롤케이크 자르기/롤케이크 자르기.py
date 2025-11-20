from collections import Counter

def solution(topping):
    answer = 0
    first_cake = dict(Counter(topping[:1]))
    second_cake = dict(Counter(topping[1:]))
    
    for next_topping in topping[1:]:
        if len(first_cake) == len(second_cake):
            answer += 1
        
        # 첫 번째 케이크에 토핑 추가
        if next_topping in first_cake:
            first_cake[next_topping] += 1
        else:
            first_cake[next_topping] = 1
        
        # 두 번째 케이크에 토핑 제거
        second_cake[next_topping] -= 1
        if second_cake[next_topping] == 0:
            del second_cake[next_topping]

    return answer