import sys
input = sys.stdin.readline

N, K = map(int, input().split())
usage = list(map(int, input().split()))

holes = []
answer = 0

for i in range(K):
    if usage[i] in holes:
        continue

    if len(holes) < N: # 멀티탭이 덜 찬 경우
        holes.append(usage[i])
        continue

    # 멀티탭에 찾는 용품이 없는 경우 -> 다음 사용이 가장 늦은 걸 뽑는다
    farthest = -1
    target = -1
    for h in holes:
        if h not in usage[i + 1:]:
            target = h
            break
        else:
            idx = usage[i + 1:].index(h)
            if idx > farthest:
                target = h
                farthest = idx
    
    holes[holes.index(target)] = usage[i]
    answer += 1

print(answer)