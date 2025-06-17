n, m = map(int, input().split())

answer = []

def backtrack(cur):
    if len(cur) == m:
        answer.append(cur[:])
        return
    for i in range(1, n+1):
        if i not in cur:
            cur.append(i)
            backtrack(cur)
            cur.pop()

backtrack([])

for a in answer:
    print(*a)