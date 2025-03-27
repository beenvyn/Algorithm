n = int(input())
periods = list(map(int, input().split()))
periods.sort(reverse=True)

current_day = 1
answer = 0
for p in periods:
    answer = max(answer, current_day + p)
    current_day += 1

print(answer + 1)