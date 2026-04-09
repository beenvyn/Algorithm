import sys
input = sys.stdin.readline

N, D = map(int, input().split())
roots = [list(map(int, input().split())) for _ in range(N)]

visited = [False] * N
answer = D

# 현재 위치, 운전한 거리
def dfs(location, dist, cnt):
    global answer
    if cnt == 0:
        answer = min(answer, dist + D - location)
        return
    
    for i in range(N):
        if not visited[i] and roots[i][0] >= location and roots[i][1] <= D:
            visited[i] = True
            dfs(roots[i][1], dist + roots[i][2] + roots[i][0] - location, cnt - 1)
            visited[i] = False
            
# 지름길 1개 ~ N개 선택하는 경우
for cnt in range(1, N + 1):
    dfs(0, 0, cnt)

print(answer)