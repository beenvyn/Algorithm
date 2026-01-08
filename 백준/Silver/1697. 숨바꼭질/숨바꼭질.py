import sys
from collections import deque
input = sys.stdin.readline

start, end = map(int, input().split())

que = deque([(start, 0)])
max_range = max(start, end) * 2 + 1
visited = [False] * max_range

while que:
    cur, time = que.popleft()

    if cur == end:
        print(time)
        break

    for x in [cur + 1, cur - 1, cur * 2]:
        if 0 <= x < max_range and not visited[x]:
            visited[x] = True
            que.append((x, time + 1))