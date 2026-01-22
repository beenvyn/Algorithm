import sys
input = sys.stdin.readline

rows, cols, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(rows)]
answer = 0

# 공격
def attack(defences):
    kill = 0
    temp_grid = [row[:] for row in grid]

    # 모든 적이 격자판에서 제외될 때까지(행의 개수만큼 내려오면 됨)
    for _ in range(rows):
        targets = []
        # 1. 궁수별 최적인 적 찾기
        for defence in defences: 
            best, best_dist = None, float('inf') # 현재 궁수의 최적 타겟

            for r in range(rows):
                for c in range(cols):
                    if temp_grid[r][c] == 1:
                        dist = abs(r - rows) + abs(c - defence)

                        if dist > d:
                            continue
                        # 더 가까운 적이거나
                        # 거리가 같으면 더 왼쪽(c가 작은) 적 선택
                        if dist < best_dist or (dist == best_dist and c < best[1]):
                            best_dist = dist
                            best = (r, c)
            if best:
                targets.append(best)

        # 2. 적 동시 제거
        # 여러 궁수가 같은 적을 노릴 수 있으므로 set으로 중복 제거
        for r, c in set(targets):
            temp_grid[r][c] = 0
            kill += 1

        # 3. 적 이동 처리(턴 종료)
        # 위에서 아래로 댕겨오고 맨 윗줄은 0으로 채우기
        for r in range(rows - 1, 0, -1):
            temp_grid[r] = temp_grid[r - 1][:]
        temp_grid[0] = [0] * cols
    
    return kill

visited = [False] * cols
# 궁수 위치 3개 고르기
def select_defense(cur):
    global answer

    if len(cur) == 3:
        answer = max(answer, attack(cur))
        return
    
    for i in range(cols):
        if not visited[i]:
            visited[i] = True
            cur.append(i)
            select_defense(cur)
            visited[i] = False
            cur.pop()

select_defense([])
print(answer)