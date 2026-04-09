import sys
input = sys.stdin.readline

string = input().rstrip()

n = string.count('a')

# 원형처리
string = string * 2

b_cnt = string[:n].count('b')
answer = b_cnt

for l in range(1, len(string) - n + 1):
    if string[l - 1] == 'b':
        b_cnt -= 1
    
    if string[l + n - 1] == 'b':
        b_cnt += 1
    
    answer = min(answer, b_cnt)

print(answer)