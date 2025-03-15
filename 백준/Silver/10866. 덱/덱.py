from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
queue = deque()

for _ in range(n):
    op = input().split()

    if len(op) > 1:
        c, num = op
        if c == 'push_back':
            queue.append(int(num))
        else:
            queue.appendleft(int(num))
    else:
        if op[0] == 'pop_front':
            print(queue.popleft()) if queue else print(-1)
        elif op[0] == 'pop_back':
            print(queue.pop()) if queue else print(-1)
        elif op[0] == 'size':
            print(len(queue))
        elif op[0] == 'empty':
            print(0) if queue else print(1)
        elif op[0] == 'front':
            print(queue[0]) if queue else print(-1)
        elif op[0] == 'back':
            print(queue[-1]) if queue else print(-1)