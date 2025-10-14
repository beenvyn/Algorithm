import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = []

def backtrack(curr):
    if len(curr) == m:
        answer.append(curr[:])
        return

    for num in range(1,n+1):
        if num not in curr:
            curr.append(num)
            backtrack(curr)
            curr.pop()

backtrack([])
for x in answer:
    print(' '.join(map(str,x)))