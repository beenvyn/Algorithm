import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [False] * n # True면 팀 A, False면 팀 B
result = sys.maxsize

def backtrack(cnt,idx): # 현재까지 팀 A에 뽑은 인원 수, 다음에 고려할 시작 인덱스
    global result

    # 팀 A가 정확히 N//2명이 되면, 팀 A/B 점수를 계산해서 차이를 갱신
    if cnt == n // 2:
        A, B = 0, 0
         # 같은 팀에 속한 (i, j) 모든 쌍에 대해 점수 합산
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]: # 둘 다 팀 A
                    A += graph[i][j]
                elif not visited[i] and not visited[j]: # 둘 다 팀 B
                    B += graph[i][j]
        
        result = min(abs(A-B), result)

    for i in range(idx,n):
        if not visited[i]: # 아직 팀 A에 안 뽑은 사람이라면
            visited[i] = True
            backtrack(cnt+1, i+1)
            visited[i] = False

# 팀 A에 0명, 인덱스 0부터 고려
backtrack(0,0)
print(result)