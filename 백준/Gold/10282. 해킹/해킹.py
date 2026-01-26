import sys
import heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append([a, s])
    
    times = [float('inf')] * (n + 1)
    times[c] = 0

    pq = [(0, c)]

    while pq:
        cur_time, u = heapq.heappop(pq)

        if cur_time > times[u]:
            continue

        for v, s in graph[u]:
            next_time = cur_time + s
            if next_time < times[v]:
                times[v] = next_time
                heapq.heappush(pq, (next_time, v))
    
    answer = [] # 감염된 컴퓨터들의 감염에 걸린 시간
    for time in times:
        if time != float('inf'):
            answer.append(time)
    
    print(len(answer), max(answer))