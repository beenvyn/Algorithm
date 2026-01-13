import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

answer = float('inf')
chickens = []
houses = []
for r in range(N):
    for c in range(N):
        if grid[r][c] == 2:
            chickens.append([r, c])
        elif grid[r][c] == 1:
            houses.append([r, c])

# 도시의 치킨 거리 구하는 함수
def get_dist(selected_chickens):
    total = 0
    for house in houses:
        min_dist = float('inf') # 집 별 치킨 거리 
        for chicken in selected_chickens:
            dist = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
            min_dist = min(dist, min_dist)
        total += min_dist
    return total

# 치킨 집 고르기
def dfs(idx, cur):
    global answer
    if len(cur) == M:
        answer = min(answer, get_dist(cur))
        return

    for i in range(idx, len(chickens)):
        cur.append(chickens[i])
        dfs(i + 1, cur)
        cur.pop()

dfs(0, [])
print(answer)