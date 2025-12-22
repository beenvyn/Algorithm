import sys
input = sys.stdin.readline

n, c = map(int, input().split()) # 마을 수, 트럭 용량
m = int(input()) # 박스 정보 개수
# (출발, 도착, 용량)
requests = [tuple(map(int, input().split())) for _ in range(m)] # 박스 정보

# 도착지 빠른 순으로 정렬
requests.sort(key=lambda x:(x[1], x[0]))

# 각 구간(i → i+1)의 남은 용량
# rem[i] : i번 마을에서 i+1번 마을로 가는 구간의 남은 용량
rem = [c] * (n + 1)
answer = 0

# 정렬된 택배 요청을 하나씩 처리
for start, end, box in requests:
    # 이 택배가 지나가는 모든 구간(start ~ end-1) 중
    # 남은 용량의 최솟값을 찾음 (병목 구간)
    possible = min(rem[i] for i in range(start, end))

    # 실제로 실을 수 있는 박스 수
    take = min(possible, box)

    # 실을 수 있다면
    if take > 0:
        # 지나가는 모든 구간의 용량에서 take 만큼 차감
        for i in range(start, end):
            rem[i] -= take

        answer += take

print(answer)