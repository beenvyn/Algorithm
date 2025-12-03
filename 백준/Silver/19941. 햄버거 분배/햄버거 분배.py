import sys

input = sys.stdin.readline
n, k = map(int, input().split())
string = list(input().rstrip())
answer = 0

for i in range(n):
    if string[i] == 'P':
        for j in range(max(0, i - k), min(n, i + k + 1)):
            if string[j] == 'H':
                answer += 1
                string[j] = 'X'
                break

print(answer)