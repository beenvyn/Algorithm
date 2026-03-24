import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
places = list(map(int, input().split()))

# 시작점 ~ 첫 가로등
h = places[0]

# 가로등 사이
for i in range(M - 1):
    dist = places[i + 1] - places[i]
    h = max(h, (dist + 1) // 2)

# 마지막 가로등 ~ 끝
h = max(h, N - places[-1])

print(h)