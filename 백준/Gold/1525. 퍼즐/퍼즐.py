import sys
from collections import deque

input = sys.stdin.readline

start = ''
for _ in range(3):
    start += ''.join(input().split())

goal='123456780'
visited = set()
next = {
    0:[1,3], 1:[0,2,4], 2:[1,5], 3:[0,4,6], 4:[1,3,5,7], 5:[2,4,8], 6:[3,7], 7:[4,6,8], 8:[5,7]
}

que = deque([(start, 0)])
visited.add(start)

while que:
    state, cnt = que.popleft()

    if state == goal:
        print(cnt)
        break
    
    zero = state.find('0')

    for n in next[zero]:
        s = list(state)
        s[zero], s[n] = s[n], s[zero]
        temp = ''.join(s)
        if temp not in visited:
            que.append((temp, cnt+1))
            visited.add(temp)

else:
    print(-1)