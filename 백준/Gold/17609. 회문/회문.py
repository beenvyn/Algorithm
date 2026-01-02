import sys
input = sys.stdin.readline

T = int(input())
words = [input().rstrip() for _ in range(T)]
answer = []

def is_pal(word, left, right):
    while left <= right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True

for i in range(T):
    word = words[i]
    left, right = 0, len(word) - 1

    while left <= right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else: # 왼쪽 문자를 하나 건너뛴 경우랑 오른쪽 문자를 하나 건너뛴 경우 중 회문이 있는지 확인 
            if is_pal(word, left + 1, right) or is_pal(word, left, right - 1):
                answer.append(1)
                break
            else:
                answer.append(2)
                break
    else:
        answer.append(0)
    
for ans in answer:
    print(ans)