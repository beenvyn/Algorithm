import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    sizes = list(map(int, input().split()))

    # prefix_sum[i]: 1번째부터 i번째까지의 합
    prefix_sum = [0] * (n+1)
    for i in range(1,n+1):
        prefix_sum[i] = prefix_sum[i-1] + sizes[i-1]
    
    # cost[start][end] = start..end 구간의 파일을 하나로 합치는 최소 비용
    cost = [[0] * (n+1) for _ in range(n+1)]

    # 길이가 length인 모든 [start, end] 구간을 왼쪽에서 오른쪽으로 순서대로 탐색하는 패턴
    for length in range(2, n+1): # 합치는 파일 개수(2부터 n까지 차례로 확장)
        for start in range(1, n-length+2):
            end = start + length - 1

            # start..end를 두 묶음 start..m, m+1..end 로 나누는 모든 분할점 m을 시도
            best = float('inf')
            for m in range(start,end):
                best = min(best, cost[start][m] + cost[m+1][end])

            # 구간 start..end의 마지막 병합 비용도 더해줌
            cost[start][end] = best + prefix_sum[end] - prefix_sum[start -1]
    
    print(cost[1][n])