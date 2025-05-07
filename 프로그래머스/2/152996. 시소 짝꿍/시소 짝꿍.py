from collections import Counter

def solution(weights):
    answer = 0
    counter = Counter(weights)
    
    for key, val in counter.items():
        if val >= 2:
            answer += val * (val - 1) // 2
    
    weights = set(weights)
    
    for w in weights:
        if w*2/3 in weights:
            answer += counter[w] * counter[w*2/3]
        if w*2/4 in weights:
            answer += counter[w] * counter[w*2/4]
        if w*3/4 in weights:
            answer += counter[w] * counter[w*3/4]
        
    return answer