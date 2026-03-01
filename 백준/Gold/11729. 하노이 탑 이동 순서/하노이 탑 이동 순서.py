import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())

moves = []
def hanoi(num, start, mid, end):
    if num == 0: # 원판이 없으면 종료
        return
    
    # 1. 위에 있는 k-1개의 원판을 보조 기둥(mid)로 옯긴다
    hanoi(num - 1, start, end, mid)

    # 2. 가장 아래의 큰 원판 1개를 목적지(end)로 옯긴다 
    moves.append((start, end))
    
    # 3. 보조 기둥에 있던 k-1개의 원판을 목적지로 옮긴다.
    hanoi(num - 1, mid, start, end)

hanoi(n, 1, 2, 3)
print(len(moves))
for a, b in moves:
    print(a, b)