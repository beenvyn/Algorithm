import sys
input = sys.stdin.readline

k = int(input())
brackests = input().rstrip().split()
answer = []

used = [False] * 10
# 현재 숫자 문자열로, 사용한 괄호 갯수
def dfs(cur, idx):
    if idx == k:
        answer.append(cur)
        return

    for n in range(10):
        if not used[n]:
            if (brackests[idx] == '<' and int(cur[-1]) < n) or (brackests[idx] == '>' and int(cur[-1]) > n):
                used[n] = True
                dfs(cur + str(n), idx + 1)
                used[n] = False
# 맨 앞에 숫자 0~9일 경우           
for i in range(10):
    used[i] = True
    dfs(str(i), 0)
    used[i] = False

answer.sort()
print(answer[-1])
print(answer[0])