import sys
input = sys.stdin.readline 

n = int(input())
string = input().rstrip()
cnt = []

# R 오른쪽으로 미는 경우
r_right = string.rstrip('R')
cnt.append(r_right.count('R'))

# B 오른쪽으로 미는 경우
b_right = string.rstrip('B')
cnt.append(b_right.count('B'))

# R 왼쪽으로 미는 경우
r_left = string.lstrip('R')
cnt.append(r_left.count('R'))

# B 왼쪽으로 미는 경우
b_left = string.lstrip('B')
cnt.append(b_left.count('B'))

print(min(cnt))