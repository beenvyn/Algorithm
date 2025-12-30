from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
infos = input().rstrip()

# 북, 동, 남, 서
# R이면 방향 인덱스 +1, L이면 -1
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir_idx = 2

visited = set() # 방문한 좌표를 모두 저장
visited.add ((0,0))
r, c = 0, 0 # (0,0)에서 시작한다고 가정

for info in infos:
    if info == 'R':
        dir_idx = (dir_idx + 1) % 4
    elif info == 'L':
        dir_idx = (dir_idx - 1) % 4
    else:
        # 'F'이면 현재 방향으로 한 칸 전진
        r += directions[dir_idx][0]
        c += directions[dir_idx][1]
        visited.add((r, c))

# visited에 찍힌 좌표들을 포함하는 범위 구하기
rows = [r for r, c in visited]
cols = [c for r, c in visited]

min_r, max_r = min(rows), max(rows)
min_c, max_c = min(cols), max(cols)

# 출력용 미로 크기
row = max_r - min_r + 1
col = max_c - min_c + 1

# 출력용 미로를 (0,0)부터 시작하도록 맞추기
# min_r = 4, max_r = 7 라면 row = 4고 인덱스는 0~3인데 이걸 그대로 찍으면 범위를 벗어남
shift_r = -min_r
shift_c = -min_c

maze = [['#'] * col for _ in range(row)]
# visited에 있는 칸들만 '.'으로 찍기
for r, c in list(visited):
    maze[r + shift_r][c + shift_c] = '.'

for r in range(row):
    print(''.join(maze[r]))
