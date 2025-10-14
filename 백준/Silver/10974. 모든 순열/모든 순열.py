import sys
input = sys.stdin.readline

n = int(input())

answer = []
def backtrack(curr):
    if len(curr) == n:
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