def solution(routes):
    # 가장 먼저 나가는 차량의 진출 지점에 카메라 설치
    # 다음 차량의 진입 지점이 현재 카메라 위치보다 작거나 같으면 → 이미 찍힘
    # 다음 차량의 진입 지점이 현재 카메라 위치보다 크면 → 기존 카메라로 못 찍으니까 새 카메라 설치
    
    routes.sort(key=lambda x:x[1])
    cur = routes[0][1]
    answer = 1
    
    for i in range(1, len(routes)):
        if routes[i][0] > cur:
            answer += 1
            cur = routes[i][1]
        
    return answer