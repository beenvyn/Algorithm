import sys
input = sys.stdin.readline

n = int(input())
ingredients = [list(map(int,input().split())) for _ in range(n)]
answer = sys.maxsize

def backtrack(cnt, idx, num, visited): # 현재까지 뽑은 재료 개수, 다음에 고려한 시작 인덱스, 뽑을 재료 개수, 방문 여부 배열(뽑는 재료 개수가 바뀔때마다 리셋)
    global answer
    if cnt == num:
        sour, bitter = 1, 0
        for j in range(n):
            if visited[j]:
                sour *= ingredients[j][0]
                bitter += ingredients[j][1]
        answer = min(answer, abs(sour-bitter))

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            backtrack(cnt+1,i+1,num,visited)
            visited[i] = False

# 재료 1개부터 n개까지 선택
for c in range(1, n+1):
    visited = [False] * n
    backtrack(0,0,c,visited)

print(answer)