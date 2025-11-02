import sys

input = sys.stdin.readline

N, d, k, c = map(int, input().split())
rail = [int(input()) for _ in range(N)]
rail.extend(rail[:k])

left = 0
answer = 0
sushi_dict = {}

# 처음에 k 만큼 고르고 시작
for i in range(k):
    if rail[i] in sushi_dict:
        sushi_dict[rail[i]] += 1
    else:
        sushi_dict[rail[i]] = 1

for right in range(k,len(rail)):
    current_sushi = rail[right]
    remove_sushi = rail[left]

    # 오른쪽으로 확장
    if current_sushi in sushi_dict:
        sushi_dict[current_sushi] += 1
    else:
        sushi_dict[current_sushi] = 1
    
    # 왼쪽으로 축소
    sushi_dict[remove_sushi] -= 1
    if sushi_dict[remove_sushi] == 0:
        del sushi_dict[remove_sushi]
    left += 1
    
    types = len(sushi_dict)
    if c not in sushi_dict:
        types += 1
    
    answer = max(answer, types)

print(answer)