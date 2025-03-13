n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
answer = [1] * n

for i in range(n):
    for j in range(n):
        if i != j:
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
                answer[i] += 1

print(*answer) 