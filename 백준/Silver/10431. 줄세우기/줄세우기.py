import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    arr = list(map(int, input().split()))
    t = arr[0]
    students = arr[1:]
    answer = 0

    que = deque([students[0]])

    for i in range(1, 20):
        if students[i] > que[-1]:
            que.append(students[i])
        else:
            temp = []
            j = len(que) - 1
            while j >= 0 and que[j] > students[i]:
                temp.append(que.pop())
                answer += 1
                j -= 1
            que.append(students[i])
            for x in temp[::-1]:
                que.append(x)
                
    print(' '.join(map(str, [t, answer])))