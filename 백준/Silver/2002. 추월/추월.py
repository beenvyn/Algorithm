import sys

input = sys.stdin.readline
n = int(input())
enter = [input() for _ in range(n)]
out = [input() for _ in range(n)]

# 차량별 들어간 순서 저장 
order = {car:idx for idx, car in enumerate(enter)}
answer = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        if order[out[j]] < order[out[i]]:
            answer += 1
            break

print(answer)