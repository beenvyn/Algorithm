import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensors = list(map(int, input().split()))

sensors = sorted(set(sensors)) # 중복 센서 제거 & 오름차순 정렬
answer = sensors[-1] - sensors[0] # 모든 센서를 하나의 집중국으로 덮었을 때의 총 길이

# 집중국이 센서 개수 이상이면 각 센서를 길이 0으로 커버 가능
if k >= len(sensors):
    print(0)
    sys.exit()

dist = [] # 센서 사이의 간격
for i in range(len(sensors) - 1):
    dist.append(sensors[i+1] - sensors[i])

dist.sort(reverse=True) # 간격 내림차순 정렬

# 가장 큰 간격 K-1개를 끊어서 전체 길이에서 빼줌
for j in range(k-1):
    answer -= dist[j]

print(answer)