import sys
from collections import Counter
input = sys.stdin.readline

t = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

# 모든 연속 부분합 구하기
def get_sub_sums(arr):
    sub_sums = []
    N = len(arr)
    for i in range(N):
        sum = 0
        for j in range(i, N):
            sum += arr[j]
            sub_sums.append(sum)
    return sub_sums
            
A_sub = get_sub_sums(A)
B_sub = get_sub_sums(B)

# 각 부분합에서 하나씩 골라서 t 만들기 
answer = 0
cntA = Counter(A_sub)

for b in B_sub:
    answer += cntA[t-b]

print(answer)