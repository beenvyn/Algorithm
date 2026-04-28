def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])
    
    visited = set([costs[0][0]]) # 시작 노드 하나 선택
    
    while len(visited) < n:
        for a, b, cost in costs:
            if a in visited and b in visited: # 이미 둘 다 연결된 경우 → 사이클 → 패스
                continue
            if a in visited or b in visited: # 한쪽만 연결된 경우
                visited.add(a)
                visited.add(b)
                answer += cost
                break # 한번에 간선 하나만 선택

    return answer