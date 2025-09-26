from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length) # 다리 위 상태
    current_weight = 0 # 다리 위 총 무게
    waiting = deque(truck_weights) # 대기열
    
    while waiting or current_weight > 0:
        time += 1
        current_weight -= bridge.popleft()
        
        if waiting and waiting[0] + current_weight <= weight:
            x = waiting.popleft()
            bridge.append(x)
            current_weight += x
        else:
            bridge.append(0)
    
    return time