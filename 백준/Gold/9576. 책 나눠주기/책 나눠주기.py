import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    people = [list(map(int, input().split())) for _ in range(M)]

    # 항상 가장 작은 번호의 책을 줘야 최적임 -> 끝이 빠른 구간부터 처리
    people.sort(key=lambda x:x[1]) # r 기준 오름차순 정렬
    used = [False] * (N + 1)
    answer = 0

    for l, r in people:
        for book in range(l, r + 1):
            if not used[book]:
                used[book] = True
                answer += 1
                break

    print(answer)