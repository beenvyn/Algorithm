import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
answer = sys.maxsize

visited = [False] * n
visited[0] = True

def backtrack(last,cnt,cost):
    global answer
    # 현재까지 비용이 최적해 이상이면 더 볼 필요 없음 (가지치기)
    if cost >= answer:
        return 

    if cnt == n:
        # 마지막에서 시작점으로 복귀 가능한지 확인
        if board[last][0] != 0:
            answer = min(answer, cost + board[last][0])
        return
    
    for nxt in range(1,n): # 0은 시작점이라 제외(고정)
        if not visited[nxt] and board[last][nxt] != 0: # last -> nxt로 가는 간선이 있어야만 진행
            visited[nxt] = True
            backtrack(nxt,cnt+1,cost + board[last][nxt])
            visited[nxt] = False

backtrack(0,1,0) # 시작 정점을 0으로 고정 → 대칭 제거
print(answer)