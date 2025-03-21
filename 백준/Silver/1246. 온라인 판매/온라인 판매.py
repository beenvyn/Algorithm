import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [int(input()) for _ in range(m)]
arr.sort()
answer = []

while arr:
    total = arr[0] * min(n, m)
    for i in range(arr.count(arr[0])):
        answer.append([total, arr[0]])
        del arr[0]
        m -= 1

answer = sorted(answer, key=lambda x:(-x[0],x[1]))
print(answer[0][1], answer[0][0])