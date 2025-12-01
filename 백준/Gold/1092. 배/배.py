import sys
input = sys.stdin.readline

N = int(input()) # 크레인 수
cranes = list(map(int,input().split()))
M = int(input()) # 박스 수
boxes = list(map(int,input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

# 모든 박스를 배로 옮길 수 없는 경우
if cranes[0] < boxes[0]:
    print(-1)
    sys.exit()

position = [0] * N # 각 크레인이 지금 보고 있는 박스 인덱스 
visited = [False] * M # 각 박스가 옮겨졌는지 여부
moved = 0 # 옮긴 박스 수
time = 0

while moved < M:
    time += 1
    for i in range(N): # 각 크레인에 대해
        while position[i] < M: # 이 크레인이 들 수 있는 박스를 찾을 때까지 인덱스를 이동
            if not visited[position[i]] and cranes[i] >= boxes[position[i]]:
                visited[position[i]] = True
                moved += 1
                position[i] += 1
                break
            else:
                # 이 박스는 못 들거나 이미 옮겼으니 다음 박스로
                position[i] += 1

print(time)