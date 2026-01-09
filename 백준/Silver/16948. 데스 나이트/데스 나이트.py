from collections import deque

def bfs(n, x1, y1, x2, y2):
    dx = [-2, -2, 0, 0, 2, 2]
    dy = [-1, 1, -2, 2, -1, 1]

    graph = [[0] * n for _ in range(n)] 

    queue = deque()
    queue.append((x1, y1))

    while queue:
        x, y = queue.popleft()

        # 도착한 경우
        if x == x2 and y == y2:
            return graph[x2][y2]
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]

            # 진입 가능 여부 확인
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if graph[nx][ny] == 0:
                    queue.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1
    
    return -1


n = int(input())
r1, c1, r2, c2 = map(int, input().split())

print(bfs(n, r1, c1, r2, c2))