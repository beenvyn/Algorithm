n, m = map(int, input().split())

answer = []

def backtrack(start, cur):
    if len(cur) == m:
        answer.append(cur[:])
        return
    for i in range(start, n+1):
        cur.append(i)
        backtrack(i+1, cur)
        cur.pop()
        
backtrack(1, [])

for a in answer:
    print(*a)