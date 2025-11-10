from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    answer = 0
    que = deque([]) 
    
    for city in cities:
        lower_city = city.lower()
        if len(que) < cacheSize: # 캐시가 덜 찬 경우
            if lower_city not in que: # miss
                que.append(lower_city)
                answer += 5
            else: # hit
                que.remove(lower_city)
                que.append(lower_city)
                answer += 1
        else:  # 캐시가 다 찬 경우
            if lower_city not in que: # miss
                que.popleft()
                que.append(lower_city)
                answer += 5
            else: # hit
                que.remove(lower_city)
                que.append(lower_city)
                answer += 1
            
    return answer