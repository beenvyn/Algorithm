import sys
input = sys.stdin.readline

N = int(input())
switches = list(map(int, input().split()))
M = int(input())
infos = [list(map(int, input().split())) for _ in range(M)]

for info in infos:
    g, num = info

    if g == 1:
        for i in range(num, N + 1, num):
            switches[i - 1] = 1 - switches[i - 1]
    else:
        num -= 1
        start, end = num, num # 중심부터 시작
        
        # 양쪽이 범위 안이고, 대칭 값이 같으면 확장
        while start - 1 >= 0 and end + 1 < N and switches[start - 1] == switches[end + 1]:
            start -= 1
            end += 1
        
        # 확정된 구간 토글
        for i in range(start, end + 1):
            switches[i] = 1 - switches[i]

for i in range(0, N, 20):
    print(' '.join(map(str, switches[i: i + 20])))