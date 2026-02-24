import sys
input = sys.stdin.readline

n = int(input())
orig = [list(map(int, input().split())) for _ in range(n)]
answer = float('inf')

# 1번 집을 r,g,b로 칠하는 세가지 경우
for first in range(3):
    costs = [row[:] for row in orig]

    # 1번 집 색상 고정 -> first만 남기고 나머지는 inf로 막기
    for c in range(3):
        if c != first:
            costs[0][c] = float('inf')

    for r in range(1, n):
        for c in range(3):
            costs[r][c] += min(costs[r-1][:c] + costs[r-1][c+1:])
    
    # 마지막 집은 first 색을 쓰면 안 됨
    answer = min(answer, min(costs[n-1][:first] + costs[n-1][first+1:]))

print(answer)