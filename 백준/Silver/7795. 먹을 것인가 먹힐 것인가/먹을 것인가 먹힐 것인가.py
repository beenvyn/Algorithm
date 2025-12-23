import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n , m = map(int, input().split())
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()))
    pointer_a, pointer_b = 0, 0
    answer = 0
    
    while pointer_a < n and pointer_b < m:
        if a[pointer_a] > b[pointer_b]:
            answer += len(a[pointer_a:])
            pointer_b += 1
        else:
            pointer_a += 1

    print(answer)