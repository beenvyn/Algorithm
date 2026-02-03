import sys
input = sys.stdin.readline

N, K = map(int, input().split())
times = [list(map(int, input().split())) for _ in range(N)]

# 모든 쌍 최단 경로 처리 (Floyd-Warshall)
for m in range(N):
    for i in range(N):
        for j in range(N):
            if times[i][j] > times[i][m] + times[m][j]:
                times[i][j] = times[i][m] + times[m][j]

answer = float('inf')
visited = [False] * N

def backtrack(cur_place, cur_time, cnt):
    global answer

    if cnt == N:
        answer = min(answer, cur_time)
        return

    for nxt in range(N):
        if not visited[nxt]:
            visited[nxt] = True
            backtrack(nxt, cur_time + times[cur_place][nxt], cnt + 1)
            visited[nxt] = False

visited[K] = True
backtrack(K, 0, 1)

print(answer)