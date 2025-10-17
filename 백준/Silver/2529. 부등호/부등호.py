import sys
input = sys.stdin.readline

k = int(input())
brackets = input().split()
visited = [False] * 10
answer = []

def check(x,y,oper):
    if oper == '<':
        return x < y
    else:
        return x > y

def backtrack(idx, cur):
    if idx == k+1:
        answer.append(cur)
        return
    
    for i in range(10):
        if not visited[i]:
            if idx == 0 or check(int(cur[idx-1]),i,brackets[idx-1]):
                visited[i] = True
                backtrack(idx+1, cur+str(i))
                visited[i] = False

backtrack(0,'')

print(max(answer))
print(min(answer))