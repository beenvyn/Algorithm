def solution(n):
    answer = []
    
    def hanoi(num, start, mid, end):
        if num == 0:
            return
        
        hanoi(num - 1, start, end, mid)
        answer.append([start, end])
        hanoi(num - 1, mid, start, end)
    
    hanoi(n, 1, 2, 3)
    return answer