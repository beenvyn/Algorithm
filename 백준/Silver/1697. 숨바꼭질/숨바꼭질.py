from collections import deque

start, end = map(int, input().split())
max_range = max(start, end) * 2 + 1
visited = [False] * max_range

q = deque([(start, 0)])
visited[start] = True

while q:
    cur_x, cnt = q.popleft()

    if cur_x == end:
        print(cnt)
        break

    for c in [cur_x - 1, cur_x + 1, cur_x * 2]:
        if 0 <= c < max_range and not visited[c]:
            q.append((c, cnt + 1))
            visited[c] = True