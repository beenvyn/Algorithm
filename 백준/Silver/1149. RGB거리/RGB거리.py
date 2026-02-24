import sys
input = sys.stdin.readline

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]

for r in range(1, n):
    for c in range(3):
        costs[r][c] += min(costs[r-1][:c] + costs[r-1][c+1:])

print(min(costs[n-1]))