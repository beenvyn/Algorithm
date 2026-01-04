import sys
input = sys.stdin.readline

N = int(input())

answer = 0
l, r = 1, 1 # r은 다음에 포함할 수
total = 0

while True:
    if total >= N:
        if total == N:
            answer += 1
        total -= l
        l += 1
    else:
        if r > N:
            break
        total += r
        r += 1

print(answer)