import sys
input = sys.stdin.readline

n, m = map(int, input().split())
books = list(map(int, input().split()))

answer = 0
left = []
right = []

# 왼쪽으로 움직이는 경우, 오른쪽으로 움직이는 경우는 따로 처리해야 되니까 음수, 양수 분리
for b in books:
    if b < 0:
        left.append(abs(b))
    else:
        right.append(b)

left.sort(reverse=True)
right.sort(reverse=True)

# m개씩 묶어서 한 번에 처리
# 각 묶음의 "가장 먼 거리"가 그 이동의 기준이 됨
for i in range(0, len(left), m):
    group = left[i:i+m]
    answer += group[0] * 2

for i in range(0, len(right), m):
    group = right[i:i+m]
    answer += group[0] * 2

# 가장 먼 거리 한 번은 왕복 안 함
# 마지막에 그 방향으로 끝내면 되기 때문
answer -= max(left[0] if left else 0, right[0] if right else 0)

print(answer)