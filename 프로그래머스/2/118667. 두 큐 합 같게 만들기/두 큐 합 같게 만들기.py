from collections import deque

def solution(que1, que2):
    t1 = sum(que1)
    t2 = sum(que2)
    total = t1 + t2

    q1 = deque(que1)
    q2 = deque(que2)
    
    max_try = (len(que1) + len(que2)) * 2
    
    for i in range(max_try):
        if t1 == t2:
            return i
            
        if t1 < t2 and len(q2) > 0:
            x = q2.popleft()
            q1.append(x)
            t2 -= x
            t1 += x
        elif t1 > t2 and len(q1) > 0:
            x = q1.popleft()
            q2.append(x)
            t1 -= x
            t2 += x

    return -1