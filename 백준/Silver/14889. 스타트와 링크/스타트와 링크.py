import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

picked = [False] * N
picked[0] = True # 0번 사람은 항상 스타트 팀 고정
answer = float('inf')

# 다음에 뽑을 사람 인덱스, 현재 뽑은 사람 수
def dfs(idx, cnt):
    global answer

    if cnt == N // 2:
        start, link = 0, 0
        for i in range(N):
            for j in range(i + 1, N):
                if picked[i] and picked[j]:
                    start += (grid[i][j] + grid[j][i])
                elif not picked[i] and not picked[j]:
                    link += (grid[i][j] + grid[j][i])
        answer = min(answer, abs(start - link))
        return

    # 조합: idx부터 사람 뽑기 시작
    for i in range(idx, N):
        if not picked[i]:
            picked[i] = True
            dfs(i + 1, cnt + 1)
            picked[i] = False

dfs(1, 1)
print(answer)