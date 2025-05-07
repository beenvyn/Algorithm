from collections import deque

def solution(x, y, n):
    graph = [0] * (y + 1)
    
    queue = deque([x])
    
    while queue:
        cur_val = queue.popleft()
        
        if cur_val == y:
            return graph[cur_val]
        for num in [cur_val + n, cur_val * 2, cur_val * 3]:
            if num <= y and not graph[num]:
                graph[num] = graph[cur_val] + 1
                queue.append(num)
                
    return -1
