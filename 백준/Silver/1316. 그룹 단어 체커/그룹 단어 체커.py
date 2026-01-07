import sys
input = sys.stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]
answer = 0

for word in words:
    chars = [word[0]]
    for i in range(1, len(word)):
        if word[i-1] != word[i]:
            if word[i] in chars: # 이전에 이미 등장한 문자면
                break
            else:
                chars.append(word[i])
    else: # 중간에 break 없이 단어를 다 돈 경우
        answer += 1
print(answer)