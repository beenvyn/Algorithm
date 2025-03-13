n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
answer = [1] * n

for i in range(n):
    for j in range(n):
        if i != j:
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
                answer[i] += 1

print(*answer) 

# 나보다 덩치 큰 애가 나타날 때 내 등수가 내려가도록 하면 된다.
