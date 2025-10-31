import sys
from collections import deque

input = sys.stdin.readline

S = int(input())

visited = set()

que = deque([(1,0,0)])
visited.add((1,0))

while que:
    screen, clip, t = que.popleft()

    if screen == S:
        print(t)
        break

    if (screen, screen) not in visited: 
        que.append((screen, screen, t+1))
        visited.add((screen,screen))
    
    if (clip + screen, clip) not in visited:
        que.append((clip + screen, clip, t+1))
        visited.add((clip + screen,clip))
    
    if (screen-1, clip) not in visited:
        que.append((screen-1, clip, t+1))
        visited.add((screen-1, clip))
