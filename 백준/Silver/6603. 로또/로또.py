import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(idx, cur):
    if len(cur) == 6:
        print(' '.join(map(str, cur)))
        return
        
    for i in range(idx, k):
        cur.append(nums[i])
        dfs(i + 1, cur[:])
        cur.pop()

while True:
    arr = list(map(int, input().split()))
    k = arr[0]
    if k == 0:
        break

    nums = arr[1:]
    dfs(0, [])
    print()