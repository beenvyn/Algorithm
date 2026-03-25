from collections import deque

def solution(cacheSize, cities):
    answer = 0
    que = deque([])
    cities = [c.lower() for c in cities]
    
    if cacheSize == 0:
        return len(cities) * 5
    
    # 가장 오래된게 왼쪽, 가장 최신게 오른쪽
    for city in cities:
        if city in que: # hit
            que.remove(city) # 기존 위치에서 제거
            que.append(city) # 가장 오른쪽으로 위치 옮김
            answer += 1
        else: # miss
            if len(que) >= cacheSize:
                que.popleft()
            que.append(city)
            answer += 5
            
    return answer