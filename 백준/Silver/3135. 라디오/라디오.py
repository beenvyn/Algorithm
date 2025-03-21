a, b = map(int, input().split())
n = int(input())
buttons = [int(input()) for _ in range(n)]

answer = 1
min_diff = abs(a - b) - 1
for button in buttons:
    if abs(button - b) < min_diff:
        min_diff = abs(button - b)

while True:
    if min_diff == 0:
        print(answer)
        break
    min_diff -= 1
    answer += 1
