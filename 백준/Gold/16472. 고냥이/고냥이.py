import sys
input = sys.stdin.readline

N = int(input())
string = input().rstrip()

answer = 0
l, r = 0, 0
ch_dict = {}

while r < len(string):
    # r 추가
    if string[r] not in ch_dict:
        ch_dict[string[r]] = 0
    ch_dict[string[r]] += 1
    r += 1
    
    while len(ch_dict.keys()) > N:
        # l 제거
        ch_dict[string[l]] -= 1
        if ch_dict[string[l]] == 0:
            del ch_dict[string[l]]
        l += 1
    
    answer = max(answer, r - l)

print(answer)