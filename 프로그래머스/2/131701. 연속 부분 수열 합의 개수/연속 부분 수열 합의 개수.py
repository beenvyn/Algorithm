def solution(elements):
    answer = set()
    extended = elements * 2
    n = len(elements)
    
    for length in range(1, n + 1):
        for i in range(n):
            result = extended[i:i+length]
            answer.add(sum(result))
            
    return len(answer)