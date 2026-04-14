import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    dic_cnt = {}

    for i in range(n):
        team = arr[i]
        if team not in dic_cnt:
            dic_cnt[team] = 0
        dic_cnt[team] += 1
    
    delete = [] # 과락인 팀
    for t in dic_cnt.keys():
        if dic_cnt[t] < 6:
            delete.append(t)
            
    rank = 1
    candidates = {}
    for i in range(n):
        team = arr[i]
        if team not in delete:
            if team not in candidates:
                candidates[team] = []
            candidates[team].append(rank)
            rank += 1

    result = [] # 상위 4명 점수, 5번째로 들어온 선수, 팀 번호
    for t in candidates.keys():
        total = sum(candidates[t][:4])
        fifth = candidates[t][4]
        result.append([total, fifth, t])

    result.sort(key=lambda x: (x[0], x[1]))
    print(result[0][2])