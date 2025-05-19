import sys
from collections import deque

input = sys.stdin.readline

n, people, g = map(int, input().split())
graph = []
infos = {}

dr = [-1,1,0,0]
dc = [0,0,-1,1]

for _ in range(n):
    graph.append(list(map(int, input().split())))

# 운전 시작 위치
sr, sc = map(int, input().split())
sr -= 1
sc -= 1

# 승객 위치 - 목적지 저장
for _ in range(people):
    a, b, c, d = list(map(int, input().split()))
    infos[(a - 1, b - 1)] = (c - 1, d - 1) # (2,2) : (5,6)

# 승객 위치 표시
for r, c in infos.keys():
    graph[r][c] = 2

# 승객 위치 탐색 -> 후보 리스트에 최단 거리 & 행 & 열 저장
def next(sr,sc):
    global g
    candidates = []
    visited = [[False] * n for _ in range(n)]

    # 현재 위치가 승객이면 바로 태움
    if graph[sr][sc] == 2:
        graph[sr][sc] = 0
        return (sr, sc)

    q = deque([(sr,sc,0)])
    visited[sr][sc] = True

    while q:
        r, c, dist = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < n and graph[nr][nc]!= 1 and not visited[nr][nc]:
                if graph[nr][nc] == 2:
                    candidates.append((dist+1,nr,nc))
                q.append((nr,nc,dist+1))
                visited[nr][nc] = True

    # 후보 승객 반환            
    if candidates:
        candidates.sort() # dist, c, r 기준으로 정렬
        dist, r, c = candidates[0]
        if g < dist:
            return None
        g -= dist
        graph[r][c] = 0 # 승객 제거
        return (r,c)
    return None

# 현재 택시 좌표 & 승객의 목적지
def move(sr,sc,er,ec):
    global g
    visited = [[False] * n for _ in range(n)]
    q = deque([(sr,sc,0)])
    visited[sr][sc] = True

    while q:
        r, c, dist = q.popleft()

        if r == er and c == ec:
            if g < dist:
                return False
            g += dist
            return True
           
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
        
            if 0 <= nr < n and 0 <= nc < n and graph[nr][nc] != 1 and not visited[nr][nc]:
                q.append((nr,nc,dist+1))
                visited[nr][nc] = True
    return False

# 시뮬레이션
for i in range(people):
    next_p = next(sr,sc)
    if next_p is None:
        print(-1)
        sys.exit()

    dest = infos[next_p]   
    if not move(next_p[0],next_p[1],dest[0],dest[1]):
        print(-1)
        sys.exit()
    
    sr, sc = dest # 택시 위치 갱신

print(g)    