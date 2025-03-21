n = int(input())
tips = [int(input()) for _ in range(n)]
tips = sorted(tips, reverse=True)

answer = 0
for idx, tip in enumerate(tips):
    total = tip - (idx + 1 - 1)
    if total > 0:
        answer += total

print(answer)