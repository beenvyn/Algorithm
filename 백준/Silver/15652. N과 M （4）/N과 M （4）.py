import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = []

def backtrack(start,curr):
    if len(curr) == m:
        answer.append(curr[:])
        return

    for num in range(start,n+1):
        curr.append(num)
        backtrack(num,curr)
        curr.pop()

backtrack(1,[])
for x in answer:
    print(' '.join(map(str,x)))