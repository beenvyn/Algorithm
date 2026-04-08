import sys
input = sys.stdin.readline

N = int(input())
roofs = [list(map(int, input().split())) for _ in range(N)]
roofs.sort(key=lambda x:x[0])

max_h = 0
for x, y in roofs:
    max_h = max(max_h, y)

# 최고 높이인 기둥 개수가 여러개인 경우 처리
left_max_i, right_max_i = 0, 0
for i in range(N):
    if roofs[i][1] == max_h:
        left_max_i = i
        break

for i in range(N - 1, -1, -1):
    if roofs[i][1] == max_h:
        right_max_i = i
        break

# 가장 높은 지붕 기준 왼쪽 넓이 구하기
l_area = 0
max_x, max_y = roofs[0][0], roofs[0][1]
for i in range(1, left_max_i + 1):
    if roofs[i][1] > max_y:
        l_area += (roofs[i][0] - max_x) * max_y
        max_x = roofs[i][0]
        max_y = roofs[i][1]

# 가장 높은 지붕 기준 오른쪽 넓이 구하기
r_area = 0
max_x, max_y = roofs[N- 1][0], roofs[N - 1][1]
for i in range(N - 2, right_max_i - 1, -1):
    if roofs[i][1] > max_y:
        r_area += (max_x - roofs[i][0]) * max_y
        max_x = roofs[i][0]
        max_y = roofs[i][1]

m_area = max_h * (roofs[right_max_i][0] - roofs[left_max_i][0] + 1)

print(l_area + r_area + m_area)