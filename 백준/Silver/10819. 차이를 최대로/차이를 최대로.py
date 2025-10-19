import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
answer = -1
visited = [False] * n

def backtrack(per):
    global answer
    if len(per) == n:
        res = 0
        for j in range(n-1):
            res += abs(per[j] - per[j+1])
        answer = max(answer, res)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            per.append(arr[i])
            backtrack(per)
            visited[i] = False
            per.pop()

backtrack([])
print(answer)