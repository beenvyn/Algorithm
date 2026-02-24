import sys
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(0)
    sys.exit()

# 에라토스테네스의 체 -> 주어진 n까지의 소수를 미리 구한다
a = [False, False] + [True] * (n-1)
prime_nums = []

for i in range(2, int(n**0.5) + 1):
    if a[i]:
        for j in range(i*i, n+1, i):
            a[j] = False

for i in range(2, n + 1):
    if a[i]:
        prime_nums.append(i)

# 투 포인터
answer = 0
prime_nums.sort()
l, r = 0, 1
total = prime_nums[0]

while True:
    if total < n:
        if r == len(prime_nums):
            break
        total += prime_nums[r]
        r += 1
    elif total >= n:
        if total == n:
            answer += 1
        total -= prime_nums[l]
        l += 1

print(answer)