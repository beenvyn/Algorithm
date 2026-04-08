import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    string = input().rstrip()
    K = int(input())

    dic = {}
    for i in range(len(string)):
        if string[i] not in dic:
            dic[string[i]] = []
        dic[string[i]].append(i)

    flag = False
    for v in dic.values():
        if len(v) >= K:
            flag = True
    
    if not flag:
        print(-1)
    else:
        min_l = len(string)
        for val in dic.values():
            for l in range(len(val) - K + 1):
                    r = l + K - 1
                    min_l = min(min_l, val[r] - val[l] + 1)
        
        max_l = 0
        for val in dic.values():
            if len(val) >= K:
                for l in range(len(val) - K + 1):
                    r = l + K - 1
                    max_l = max(max_l, val[r] - val[l] + 1)

        print(min_l, max_l)
