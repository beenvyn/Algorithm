import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    arr = []
    t = int(input())
    cur = input()
    goal = input()

    for i in range(t):
        if cur[i] != goal[i]:
            arr.append(cur[i])
    
    if arr.count('W') > arr.count('B'):
        print(arr.count('W'))
    else:
        print(arr.count('B'))
