from collections import deque

n = int(input())
queue = deque(range(1, n + 1))
answer = []

while len(queue) > 1:
    answer.append(queue.popleft())
    x = queue.popleft()
    queue.append(x)

answer.append(queue.popleft())
print(*answer)