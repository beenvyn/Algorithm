import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [input().rstrip() for _ in range(n)]
memo = { w: 0 for w in arr }
answer = 0

for i in range(m):
    words = input().rstrip().split(',')

    for word in words:
        if word in memo.keys():
            if memo[word] == 0:
                answer += 1
                memo[word] += 1

    print(n - answer)