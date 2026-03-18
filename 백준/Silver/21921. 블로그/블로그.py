import sys
input = sys.stdin.readline

N, X = map(int, input().split())
cnts = list(map(int, input().split()))

l, r = 0, X
cur_cnt = sum(cnts[:X])

max_cnt = cur_cnt
period = 1

while r < N:
    cur_cnt -= cnts[l]
    cur_cnt += cnts[r]

    if cur_cnt > max_cnt:
        max_cnt = cur_cnt
        period = 1
    elif cur_cnt == max_cnt:
        period += 1
    
    l += 1
    r += 1

if max_cnt == 0:
    print('SAD')
else:
    print(max_cnt)
    print(period)