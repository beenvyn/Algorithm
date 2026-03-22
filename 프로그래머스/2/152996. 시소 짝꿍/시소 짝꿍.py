import math

def solution(weights):
    answer = 0
    weights.sort()
    
    # 현재 몸무게와 짝이 되는 이전 몸무게가 몇 개 있었는지 세기
    # cnt_dict[몸무게] = 지금까지 나온 개수
    cnt_dict = {} 
    
    # 가능한 비율 후보: 1:1, 2:3, 1:2(2:4), 3:4
    
    for w in weights:
        if w in cnt_dict:
            answer += cnt_dict[w]
        
        if (w * 2) % 3 == 0:
            target = (w * 2) // 3
            if target in cnt_dict:
                answer += cnt_dict[target]
        
        if w % 2 == 0:
            target = w // 2
            if target in cnt_dict:
                answer += cnt_dict[target]
        
        if (w * 3) % 4 == 0:
            target = (w * 3) // 4
            if target in cnt_dict:
                answer += cnt_dict[target]
        
        if w not in cnt_dict:
            cnt_dict[w] = 0
        cnt_dict[w] += 1    
    
    return answer